# stackoverflow-lite API


[![Build Status](https://travis-ci.com/MRichardN/stackoverflow_lite_api.svg?branch=develop)](https://travis-ci.com/MRichardN/stackoverflow_lite_api)
[![Maintainability](https://api.codeclimate.com/v1/badges/e8e354303b4f111a8781/maintainability)](https://codeclimate.com/github/MRichardN/stackoverflow_lite_api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/MRichardN/stackoverflow_lite_api/badge.svg?branch=develop)](https://coveralls.io/github/MRichardN/stackoverflow_lite_api?branch=develop)

The api enables you to:
            - test endpoints (GET, POST, PUT, DELETE)
            - create and register a user within the application.




# Starting the application
Run the following commands inorder to set the environment and start the application respectively
```
export SECRET="input some random string"

export APP_SETTINGS="development"

export FLASK_APP=run.py

flask run
```
#API-endpoints
* GET `/api/v1/questions/1` : Get a single question
* GET `/api/v1/questions` : Get all questions
* POST `/api/v1/questions` : Post questions
* PUT `/api/v1/question` 
* DELETE


# questions
The user is  able to create and get back a list of their questions.
The user can create, delete, request, and update questions


# Running tests
Before running the application tests, update your environment variables
```
export  APP_SETTINGS=app.config.TestingConfig

```


# Running tests with coverage
Run tests with coverage by running this command in the terminal
```
nosetests 

nosetests --with-coverage --cover-package=app
```