import os
import logging


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = ''
    LOG_FORMAT = '%(asctime)s:%(name)s:%(levelname)s:%(message)s'
    LOG_ROOT = '//logs'
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_PATH = os.environ.get('LOG_PATH', 'logs/googlespreadsheet.log')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_BINDS = {
        'dgtech': ''
    }

class ProductionConfig(BaseConfig):
    DEBUG = True
    LOG_PATH = os.environ.get('LOG_PATH', 'logs/googlespreadsheet.log')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_BINDS = {
        'dgtech': ''
    }