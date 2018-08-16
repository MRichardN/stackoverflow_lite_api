#app/views.py

from app.__init__ import create_app
#import json
from flask import Flask
from flask import request, jsonify, abort, make_response

#from instance.config import app_config


#@app.errorhandler(404)
#def not_found(error):
 #   return make_response(jsonify({'error': 'Not found'}), 404)

app = Flask(__name__)

questions = [
    {
        'id': 1,
        'language': 'python',
        'ask':'How do we install python3 in a virtual environment',
        'date_posted': '7th July, 2018'
        
    },
    {
        'id': 2,
        'language': 'python',
        'ask':'How to run flask',
        'date_posted': '10th May, 2018'
    }
]


#GET all questions
#@app.route('/app/api/v1/questions', methods=['GET'])
#def get_questions():
#    return jsonify({'questions': questions})

  

#GET a single question app/api/v1/questions/<int:question_id>
@app.route('/stack/api/v1/questions', methods=['GET'])
def get_question(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    return jsonify({'question': question[0]})    

#POST
@app.route('/app/api/v1/questions', methods=['POST'])
def create_question():
    if not request.json or not 'language' in request.json:
        abort(400)
    question = {
        'id': tasks[-1]['id'] + 1,
        'language': request.json['language'],
        'date_posted': request.json.get('date_posted', "")
    }
    questions.append(question)
    return jsonify({'question': question}), 201  

#PUT
@app.route('/app/api/v1/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'language' in request.json and type(request.json['language']) != unicode:
        abort(400)
    if 'ask' in request.json and type(request.json['ask']) is not unicode:
        abort(400)
    if 'date_posted' in request.json and type(request.json['date_posted']) is not unicode:
        abort(400)
    task[0]['language'] = request.json.get('language', task[0]['language'])
    task[0]['ask'] = request.json.get('ask', task[0]['ask'])
    task[0]['date_posted'] = request.json.get('date_posted', task[0]['date_posted'])
    return jsonify({'question': question[0]})

@app.route('/app/api/v1/questions/<int:question_id>', methods=['DELETE'])
def delete_question(task_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    questions.remove(question[0])
    return jsonify({'result': True})     

if __name__ == '__main__':
    app.run(debug=True)