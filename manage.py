import math
import sys

from app import create_app
from flask_socketio import SocketIO
from flask_script import Manager,Shell
from dependency.util import Server
from app.realtimemonitor.scan_zdt import get_zg_code
import tushare as ts

async_mode = "threading"

app = create_app('default')

# 打开调试功能
# manager.add_command('runserver',Server(use_debugger=True))
socketio = SocketIO(app, async_mode=async_mode)
socketio.init_app(app, cors_allowed_origins='*')

@socketio.on('start_monitor',namespace='/test')
def test_message():
    print('receive')
    # print(message)
    # 定时任务
    zg_code_dict = get_zg_code()
    code_list = list(zg_code_dict.keys())
    conn=ts.get_apis()

    each_batch = math.ceil(len(code_list)/5)
    # 分批 3批
    while 1:

        for i in range(5):
            code_list_=code_list[i*each_batch:each_batch*(i+1)]

            try:
                df = ts.quotes(code_list_,conn=conn)
            except Exception as e:
                socketio.sleep(10)
                continue

            df=df[['code','price','last_close']]
            df['percent']=df.apply(lambda row:round((row['price']-row['last_close'])/row['last_close']*100,2),axis=1)
            df=df[(df['percent']>8) | (df['percent']<-8)]
            df=df.sort_values(by='percent')
            df['name']=df['code'].map(lambda x:zg_code_dict.get(x))

            if len(df)>0:
                result=df.to_dict(orient='records')
                print('send---')
                # print(result)
                # for item in result:

                socketio.emit('start_response', {'data':result,'num':i+1},namespace="/test")

            # socketio.sleep(60)


@socketio.on('stop_monitor',namespace='/test')
def test_message():
    print('receive')
    # print(message)
    socketio.emit('stop_response',{'data':'nihao'} ,namespace="/test")

manager = Manager(app)


def make_shell_context():
    return dict(app=app)

manager.add_command('shell',Shell(make_context=make_shell_context))
server=Server()
server.get_socket(socketio)
manager.add_command("runserver", server)

if __name__=='__main__':
    # socketio.run(app)
    manager.run()
