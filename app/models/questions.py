from flask import jsonify
from datetime import datetime
import psycopg2

class  Question(object):
	"""docstring for  Questions"""
	current_id=0
	questions = []
	def __init__(self, language=None, ask=None):
		self.language = language
		self.ask = ask
		self.date_posted = None

	def create(self, language,ask):
		self.current_id += 1
		new_question = {
			'question_id':self.current_id,
            'language':language,
            'ask': ask,
            'date_posted': datetime.now(),
        }
		self.questions.append(new_question)
		return jsonify(new_question)

	def all(self):
		return jsonify(self.questions)

	def view(self, id):
		return jsonify(id)