import sys

from app import create_app
from flask_socketio import SocketIO
from flask_script import Manager,Shell
from dependency.util import Server
async_mode = "threading"

app = create_app('default')

# 打开调试功能
# manager.add_command('runserver',Server(use_debugger=True))
socketio = SocketIO(app, async_mode=async_mode)
socketio.init_app(app, cors_allowed_origins='*')

@socketio.on('monitor',namespace='/test')
def test_message(message):
    print('receive')

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
