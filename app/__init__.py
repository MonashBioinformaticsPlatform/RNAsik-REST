# -*- coding: utf-8 -*-
from flask import Flask


import api


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        api.bp,
        url_prefix='/api')
    
    @app.after_request
    def after_request(response):
      response.headers.add('Access-Control-Allow-Origin', '*')
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
      return response    
    
    return app

if __name__ == '__main__':
    create_app().run(debug=True)