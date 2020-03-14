# -*-coding=utf-8-*-

# @Time : 2020/3/12 18:05
# @File : util.py
import sys
from flask_script.commands import Command

class Option(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class Server(Command):

    help = description = 'Runs the Flask development server i.e. app.run()'

    def __init__(self, host='127.0.0.1', port=5000, use_debugger=None,
                 use_reloader=None, threaded=False, processes=1,
                 passthrough_errors=False, ssl_crt=None, ssl_key=None, **options):

        self.port = port
        self.host = host
        self.use_debugger = use_debugger
        self.use_reloader = use_reloader if use_reloader is not None else use_debugger
        self.server_options = options
        self.threaded = threaded
        self.processes = processes
        self.passthrough_errors = passthrough_errors
        self.ssl_crt = ssl_crt
        self.ssl_key = ssl_key
        self.socketio=None


    def get_options(self):

        options = (
            Option('-h', '--host',
                   dest='host',
                   default=self.host),

            Option('-p', '--port',
                   dest='port',
                   type=int,
                   default=self.port),

            Option('--threaded',
                   dest='threaded',
                   action='store_true',
                   default=self.threaded),

            Option('--processes',
                   dest='processes',
                   type=int,
                   default=self.processes),

            Option('--passthrough-errors',
                   action='store_true',
                   dest='passthrough_errors',
                   default=self.passthrough_errors),

            Option('-d', '--debug',
                   action='store_true',
                   dest='use_debugger',
                   help='enable the Werkzeug debugger (DO NOT use in production code)',
                   default=self.use_debugger),
            Option('-D', '--no-debug',
                   action='store_false',
                   dest='use_debugger',
                   help='disable the Werkzeug debugger',
                   default=self.use_debugger),

            Option('-r', '--reload',
                   action='store_true',
                   dest='use_reloader',
                   help='monitor Python files for changes (not 100%% safe for production use)',
                   default=self.use_reloader),
            Option('-R', '--no-reload',
                   action='store_false',
                   dest='use_reloader',
                   help='do not monitor Python files for changes',
                   default=self.use_reloader),
            Option('--ssl-crt',
                   dest='ssl_crt',
                   type=str,
                   help='Path to ssl certificate',
                   default=self.ssl_crt),
            Option('--ssl-key',
                   dest='ssl_key',
                   type=str,
                   help='Path to ssl key',
                   default=self.ssl_key),
        )

        return options
    def get_socket(self,socketio):
        self.socketio=socketio
    def __call__(self,app, host, port, use_debugger, use_reloader,
                 threaded, processes, passthrough_errors, ssl_crt, ssl_key):
        # we don't need to run the server in request context
        # so just run it directly

        if use_debugger is None:
            use_debugger = app.debug
            if use_debugger is None:
                use_debugger = True
                if sys.stderr.isatty():
                    print("Debugging is on. DANGER: Do not allow random users to connect to this server.", file=sys.stderr)
        if use_reloader is None:
            use_reloader = use_debugger

        if None in [ssl_crt, ssl_key]:
            ssl_context = None
        else:
            ssl_context = (ssl_crt, ssl_key)

        self.socketio.run(app,
                     host=host,
                     port=port,
                     debug=use_debugger,
                     use_reloader=use_reloader,
                     **self.server_options)
