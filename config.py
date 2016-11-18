# Builtin config values: http://flask.pocoo.org/docs/0.10/config/
import os

DEBUG = os.environ.get('DEBUG', False)
HOST = os.environ.get('HOST', 'localhost')
PORT = int(os.environ.get('PORT', 5000))

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_LOCATION = 'jinja2-live-parser.log'
LOGGING_LEVEL = 'DEBUG'
