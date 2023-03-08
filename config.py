class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pizza.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_HERE = '249y823r9v8238r9u'
    RESTX_JSON = {'ensure_ascii': False, 'indent': 3}