from flask import render_template,jsonify
from . import main

@main.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')

@main.route('/test',methods=['POST','GET'])
def test():
    return jsonify({'status':200,'msg':'Test page'})