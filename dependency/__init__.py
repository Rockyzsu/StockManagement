# -*-coding=utf-8-*-

# @Time : 2020/3/12 17:51
# @File : __init__.py.py
import sys

from flask_script.commands import Command

class Option(object):
    """
    Stores positional and optional arguments for `ArgumentParser.add_argument
    <http://argparse.googlecode.com/svn/trunk/doc/add_argument.html>`_.

    :param name_or_flags: Either a name or a list of option strings,
                          e.g. foo or -f, --foo
    :param action: The basic type of action to be taken when this argument
                   is encountered at the command-line.
    :param nargs: The number of command-line arguments that should be consumed.
    :param const: A constant value required by some action and nargs selections.
    :param default: The value produced if the argument is absent from
                    the command-line.
    :param type: The type to which the command-line arg should be converted.
    :param choices: A container of the allowable values for the argument.
    :param required: Whether or not the command-line option may be omitted
                     (optionals only).
    :param help: A brief description of what the argument does.
    :param metavar: A name for the argument in usage messages.
    :param dest: The name of the attribute to be added to the object
                 returned by parse_args().
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class Server(Command):
    """
    Runs the Flask development server i.e. app.run()

    :param host: server host
    :param port: server port
    :param use_debugger: Flag whether to default to using the Werkzeug debugger.
                         This can be overriden in the command line
                         by passing the **-d** or **-D** flag.
                         Defaults to False, for security.

    :param use_reloader: Flag whether to use the auto-reloader.
                         Default to True when debugging.
                         This can be overriden in the command line by
                         passing the **-r**/**-R** flag.
    :param threaded: should the process handle each request in a separate
                     thread?
    :param processes: number of processes to spawn
    :param passthrough_errors: disable the error catching. This means that the server will die on errors but it can be useful to hook debuggers in (pdb etc.)
    :param ssl_crt: path to ssl certificate file
    :param ssl_key: path to ssl key file
    :param options: :func:`werkzeug.run_simple` options.
    """

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

    def __call__(self, app, host, port, use_debugger, use_reloader,
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

        socketio.run(app,
                     host=host,
                     port=port,
                     debug=use_debugger,
                     use_reloader=use_reloader,
                     **self.server_options)
