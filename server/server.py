import argparse

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_compress import Compress

db = SQLAlchemy()
migrate = Migrate()
compress = Compress()

class AttrDict(dict):
    """ Easy dictionary class """

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self

def build_app(conf):
    """ Build application with the given information

    :param conf:    Configuration
    :return:        application

    """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = conf.SQLALCHEMY_DATABASE_URL
    app.config["TESTING"] = conf.TESTING
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    CORS(app)

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

    db.init_app(app)
    compress.init_app(app)
    migrate.init_app(app, db)

    api = Api(app)

    # add view to restful api
    from resource.cate import CategoryView
    from resource.item import ItemView
    from resource.mall import ShoppingMallView

    api.add_resource(CategoryView, "/cate")
    api.add_resource(ItemView, "/item/<ft>/<date>/<time>/<asc>")
    api.add_resource(ShoppingMallView, "/mall")

    return app

if __name__ == "__main__":
    app = build_app(AttrDict(
        SQLALCHEMY_DATABASE_URL="sqlite:///database.db",
        TESTING=False
    ))
    app.run(debug=True)