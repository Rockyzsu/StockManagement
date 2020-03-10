from flask import Flask
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

def create_app(config):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234567890'
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    from .fund import fund as fund_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(fund_blueprint,url_prefix='/fund')

    return app