# config.py
import os

DEBUG = False
SECRET_KEY = '2waefas1234safq2r'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'reminders.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
