import os
from redis import Redis
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('APP_SECRET_KEY') or 'hard to guess string'
    BCRYPT_LOG_ROUNDS = 12
    CACHE_TYPE = os.environ.get('CACHE_TYPE') or 'redis'
    CACHE_REDIS_URL = f'redis://{os.getenv("REDIS_CONFIG")}:{os.getenv("REDIS_PORT")}/0'
    SESSION_TYPE = os.environ.get('SESSION_TYPE') or 'redis'
    SESSION_USE_SIGNER = True  # Optional: Enable session data signing for security
    SESSION_PERMANENT = False  # Optional: Set session to expire when the browser is closed
    SESSION_KEY_PREFIX = 'session:'  # Optional: Prefix for session keys in Redis
    SESSION_REDIS = Redis(host=os.getenv('REDIS_CONFIG'), port=os.getenv('REDIS_PORT'))  # Redis connection details
    RATE_LIMIT = 5  # Maximum requests allowed within the time window (per user)
    RATE_LIMIT_PERIOD = 10  # Time window in seconds
    REDIS_HOST = os.getenv('REDIS_CONFIG')
    REDIS_PORT = os.getenv('REDIS_PORT')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentContainerConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')


class DevelopmentlocalConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_LOCAL_DATABASE_URL')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


# class HerokuConfig(ProductionConfig):
    # SSL_REDIRECT = True if os.environ.get('DYNO') else False

    # @classmethod
    # def init_app(cls, app):
    #     ProductionConfig.init_app(app)

    #     # handle reverse proxy server headers
    #     try:
    #         from werkzeug.middleware.proxy_fix import ProxyFix
    #     except ImportError:
    #         from werkzeug.contrib.fixers import ProxyFix
    #     app.wsgi_app = ProxyFix(app.wsgi_app)

    #     # log to stderr
    #     import logging
    #     from logging import StreamHandler
    #     file_handler = StreamHandler()
    #     file_handler.setLevel(logging.INFO)
    #     app.logger.addHandler(file_handler)


class DockerConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


class UnixConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to syslog
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.INFO)
        app.logger.addHandler(syslog_handler)


config = {
    'development': DevelopmentContainerConfig,
    'development_local': DevelopmentlocalConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    # 'heroku': HerokuConfig,
    'docker': DockerConfig,
    'unix': UnixConfig,

    'default': DevelopmentContainerConfig
}
