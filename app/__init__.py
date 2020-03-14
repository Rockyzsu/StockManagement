from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment

bootstrap = Bootstrap()
moment = Moment()

def create_app(config):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234567890'

    bootstrap.init_app(app)
    moment.init_app(app)


    from .main import main as main_blueprint
    from .fund import fund as fund_blueprint
    from .cb import cb as cb_blueprint
    from .jingzhi import jingzhi as jingzhi_blueprint
    from .realtimemonitor import realtime as realtime_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(fund_blueprint,url_prefix='/fund')
    app.register_blueprint(cb_blueprint,url_prefix='/cb')
    app.register_blueprint(jingzhi_blueprint,url_prefix='/jz')
    app.register_blueprint(realtime_blueprint,url_prefix='/rt')

    return app
