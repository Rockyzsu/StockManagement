from flask import Flask
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

def create_app(config):
    app = Flask(__name__)
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    from .fund import fund as fund_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(fund_blueprint)

    return app