 #app/models.py

from app import db

class Question(db.Model):
    """This class represents the questions table."""

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(255))
    ask = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=db.func.current_timestamp())
    

    def __init__(self, language):
        """initialize with language."""
        self.language = language

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Question.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Question: {}>".format(self.name)




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

manager.add_command('db', MigrateComma
nd)

if __name__ == '__main__':
  manager.run()



'''
'''
import psycopg2
from pprint import pprint

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='postgresdemo' user='hoangnd' host='localhost' password='123456' port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Cannot connect to database")

    def create_table(self):
        create_table_command = "CREATE TABLE pet(id serial PRIMARY KEY, name varchar(100), age integer NOT NULL)"
        self.cursor.execute(create_table_command)

    def insert_new_record(self):
        new_record = ("misa meo6", "6")
        insert_command = "INSERT INTO pet(name, age) VALUES('" + new_record[0] + "','" + new_record[1] + "')"
        pprint(insert_command)
        self.cursor.execute(insert_command)

    def query_all(self):
        self.cursor.execute("SELECT * FROM pet")
        cats = self.cursor.fetchall()
        for cat in cats:
            pprint("each pet : {0}".format(cat))

    def update_record(self):
        update_command = "UPDATE pet SET age=10 WHERE id=1"
        self.cursor.execute(update_command)

    def drop_table(self):
        drop_table_command = "DROP TABLE pet"
        self.cursor.execute(drop_table_command)

if __name__== '__main__':
    database_connection = DatabaseConnection()
    # database_connection.create_table()
    # database_connection.insert_new_record()
    # database_connection.query_all()
    # database_connection.update_record()
    database_connection.drop_table()

#######
import os
import psycopg2
from flask import Flask, render_template
import urlparse
from os.path import exists
from os import makedirs

url = urlparse.urlparse(os.environ.get('DATABASE_URL'))
db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
schema = "schema.sql"
conn = psycopg2.connect(db)

cur = conn.cursor()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/contacts')
def contacts():
    try:
        cur.execute("""SELECT name from salesforce.contact""")
        rows = cur.fetchall()
        response = ''
        my_list = []
        for row in rows:
            my_list.append(row[0])

        return render_template('template.html',  results=my_list)
    except Exception as e:
        print e
        return []

if __name__ == '__main__':
    app.run()
'''






