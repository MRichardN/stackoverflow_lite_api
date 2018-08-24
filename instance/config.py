#instance/config.py

import os

class Config(object):
    #Parent configuration class
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
   # PSYCOPG2_DATABASE_URI = os.getenv('DATABASE_URL')
    #PSYCOPG2_DATABASE_URI=”pgsql://dbuser:dbpassword@dbhost/database”
    
class DevelopmentConfig(Config):
    #Configurations for Development.
    DEBUG = True

    

class TestingConfig(Config):
    #Configurations for Testing.
    TESTING = True
    DEBUG = True
    #PSYCOPG2_DATABASE_URI = 'postgresql://localhost/test_db'

class StagingConfig(Config):
    #Configurations for Staging.
    DEBUG = True

class ProductionConfig(Config):
   # Configurations for Production.
    DEBUG = False
    TESTING = False
    
#conn  = psycopg2.connect(host="localhost",database="stackoverflow", user="postgres", password="root")
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}


params = {
        'host' :'localhost',
        'database' :'stackoverflow',
        'user':'postgres',
        'password':'root'
    }


