import os
import logging
import logging.config


log = logging.getLogger(__name__)


class DatabaseConfig:
    DB_DIALECT = 'postgresql'
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_USER = 'postgres'
    DB_PASSWORD = 'a'
    DB_NAME = 'crickbuzz'


class BaseConfig(DatabaseConfig):
    APP_NAME = 'crickbuzz'
    DEBUG = False
    RESTX_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTX_VALIDATE = True
    RESTX_MASK_SWAGGER = False
    RESTX_ERROR_404_HELP = False
    SWAGGER_UI_JSONEDITOR = False

    LOG_CONFIG_PATH = 'C:\\Users\\Richa\\PycharmProjects\\crickbuzz\\cricbuzz\\logging.conf'


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True


class TestingConfig(BaseConfig):
    ENV = 'testing'
    DEBUG = True


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
