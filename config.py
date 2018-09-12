import os

class Config:
    '''parent configuration class .'''
    pass

class DevelopmentConfig(Config):
    '''configurations for development'''
    DEBUG = True

class TestingConfig(Config):
    '''configurations for Testing'''
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    '''configurations for Production'''
    DEBUG = False
    TESTING = False

app_config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
