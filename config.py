# config.py
import os

DEBUG = False
SECRET_KEY = '2waefas1234safq2r'

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DBTYPE') == "mem":
    LOCAL_DB = "sqlite://"
else:
    LOCAL_DB = 'sqlite:///' + os.path.join(basedir, 'reminders.db')

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or LOCAL_DB

SQLALCHEMY_TRACK_MODIFICATIONS = False
