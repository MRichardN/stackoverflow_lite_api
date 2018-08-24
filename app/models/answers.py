from flask import jsonify
from datetime import datetime
import psycopg2

class Answer(object):
	"""docstring for answers"""
	current_id=0
	answers = []
	def __init__(self, language=None, ask=None):
		self.language = language
		self.ask = ask
		self.dateposted = None
	
	def create(self, question_id, ask, language):
		self.current_id += 1
		new_answer = {
			'id': self.current_id,
			'question_id': question_id,
			'ask': ask,
			'language': language,
			'dateposted': datetime.now(),
		}
		self.answers.append(new_answer)
		return new_answer
'''

def create(self, question_id, ask, language):
    con=psycopg2.connect(((**params)))
    cursor=con.cursor()

    cursor.execute("insert into answers(ask,lang) values()")
    con.commit

	'''