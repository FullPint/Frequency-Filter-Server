from flask import Flask
import os
from Filtering_Server.Front_End import Front_End

def create_app():
    app = Flask(__name__)
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    app.config['root'] = APP_ROOT
    app.config['FOO'] = os.path.join(APP_ROOT, 'static')
    APP_UPLOADS = os.path.join(APP_ROOT, 'static/Images')
    app.config['UPLOAD_FOLDER'] = APP_UPLOADS
    app.config['SECRET_KEY'] = 'secret'
    app.register_blueprint(Front_End)
    return app
