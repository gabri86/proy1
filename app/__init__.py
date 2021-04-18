import os

#from config import basedir #descomentar cuando se complete el archivo de configuarcion
from flask import Flask

app = Flask(__name__)

from app import views, models

