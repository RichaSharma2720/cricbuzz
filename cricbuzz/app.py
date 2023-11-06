from flask import Flask
from cricbuzz.config import config_by_name
from cricbuzz.model.db import db
from cricbuzz.api import api_v1
from cricbuzz.utils.error_handlers import not_found_error, global_error_handler
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
import cricbuzz.model.models
import logging
# import logging.config

# log = logging.getLogger(__name__)

def create_app(config_name='dev'):
    config = config_by_name[config_name]
    app = Flask(config.APP_NAME)

    app.register_error_handler(404, not_found_error)
    app.register_error_handler(Exception, global_error_handler)

    app.config.from_object(config)
    app.register_blueprint(api_v1)

    logging.config.fileConfig(app.config.get('LOG_CONFIG_PATH'))

    db_connection_uri = f"{config.DB_DIALECT}://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_connection_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False

    db.init_app(app)

    engine = create_engine(db_connection_uri)
    logging.info("Checking if database exists...")
    if not database_exists(engine.url):
        logging.info("Creating database...")
        create_database(engine.url)

    setup_db(app)
    return app


def setup_db(app):
    logging.info("creating database tables if not exists...")
    with app.app_context():
        db.create_all()

def main():
    app = create_app('dev')
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port, DEBUG = True)


if __name__ == '__main__':
    main()
