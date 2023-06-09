"""Application Configuration."""
import os


class Config(object):
    """Parent configuration class."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')

    TITLE = "Flask API with Celery"
    VERSION = "0.1.0"
    DESCRIPTION = "An API Skeleton with Celery."

    CELERY_BROKER_URL = "amqp://myuser:mypassword@localhost:5672"
    CELERY_RESULT_BACKEND = 'rpc://'
    BROKER_URL = CELERY_BROKER_URL


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing."""

    TESTING = True
    DEBUG = True

    CELERY_ALWAYS_EAGER = True


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False

    CELERY_BROKER_URL = "amqp://myuser:mypassword@localhost:5672"
    CELERY_RESULT_BACKEND = 'rcp://'
    BROKER_URL = CELERY_BROKER_URL


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
