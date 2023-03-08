from flask import Flask

from pizza.config import Config
from pizza.setup_db import db
from pizza.views.buy import buy_blueprint
from pizza.views.home import home_blueprint
from pizza.views.product import product_blueprint


# функция создания основного объекта app


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_blueprints(app)
    return app

def register_blueprints(app):
    db.init_app(app)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(product_blueprint)
    app.register_blueprint(buy_blueprint)

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()
