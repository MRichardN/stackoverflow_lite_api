#app/views.py

from app.__init__ import create_app

from flask import Flask
from flask import request, jsonify, abort, make_response


app = Flask(__name__, instance_relative_config=True)
            

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
@app.route('/app/api/v1/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': questions})

  

#GET a single question 
@app.route('/app/api/v1/questions/<int:question_id>', methods=['GET'])
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
        'id': questions[-1]['id'] + 1,
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
    #if 'id' in request.json and type(request.json['id']) != unicode:
       # abort(400)    
    if 'language' in request.json and type(request.json['language']) != unicode:
        abort(400)
    if 'ask' in request.json and type(request.json['ask']) is not unicode:
        abort(400)
    if 'date_posted' in request.json and type(request.json['date_posted']) is not unicode:
        abort(400)
    question[0]['id'] = request.json.get('id', question[0]['id'])    
    question[0]['language'] = request.json.get('language', question[0]['language'])
    question[0]['ask'] = request.json.get('ask', question[0]['ask'])
    question[0]['date_posted'] = request.json.get('date_posted', question[0]['date_posted'])
    return jsonify({'question': question[0]})

    

@app.route('/app/api/v1/questions/<int:question_id>', methods=['DELETE'])
def delete_question(task_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    questions.remove(question[0])
    return jsonify({'result': True})   



users =[]

@app.route('/app/api/v1/sign_up', methods=['POST'])
def sign_up():
    user = {'id': len(users)+1,
        'user_name': request.json.get('user_name'),
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    users.append(user)
    return jsonify({'message': 'Registration successful', 'User': users}), 201

@app.route('/app/api/v1/login', methods=['POST'])
def signin():
    user_name= request.json.get("user_name")
    password= request.json.get("password")

    if user_name == "" or password == "":
        return "Please enter your user_name and password to log in"
    user = [user for user in users if user['user_name'] == user_name and user['password'] == password]

    if not user:
        return jsonify({'message': 'New user?, Please sign_up'})
    return jsonify({'message': 'Logged in successsfully'})      

if __name__ == '__main__':
    app.run(debug=True)