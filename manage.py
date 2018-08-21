
'''
import os
import psycopg2

conn = psycopg2.connect('dbname='testdb' user='postgres' host='localhost' password='my_password')

conn = psycopg2.connect(host="localhost",database="suppliers", user="postgres", password="postgres")
cur = con.cursor()






con.commit()
cur.close()
con.close()

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app import models



app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()



'''









