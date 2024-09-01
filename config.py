from sqlalchemy.testing.plugin.plugin_base import config


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class ProductioConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask:246@localhost:5432/posts'


config_options = {
    'pro': ProductioConfig,
    'dev': DevelopmentConfig,
}