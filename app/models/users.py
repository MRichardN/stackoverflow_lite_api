from flask import jsonify
from datetime import datetime
import psycopg2

class User(object):
    current_id = 0
    users = []

    def create(self, username, email, password):
        self.current_id +=1
        new_user = {
            'user_id': self.current_id,
            'user_name': username,
            'email': email,
            'password': password,
        }

        self.users.append(new_user)

        return self.users