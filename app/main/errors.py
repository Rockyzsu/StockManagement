from . import main
from flask import jsonify
@main.app_errorhandler(404)
def page_not_found(e):
    return jsonify({'status':404,'msg':'404 Page not found!'})

@main.app_errorhandler(500)
def internal_server(e):
    return jsonify({'status':200,'msg':'500 internal server error!'})
