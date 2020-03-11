from app import create_app
from flask_script import Manager,Shell,Server
app = create_app('default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app)

manager.add_command('shell',Shell(make_context=make_shell_context))
# 打开调试功能
# manager.add_command('runserver',Server(use_debugger=True))


if __name__=='__main__':
    manager.run()
