from flask import Flask
app = Flask(__name__)
app_wsgi = Flask.wsgi_app

from app import routes