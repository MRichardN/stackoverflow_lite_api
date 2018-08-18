# stackoverflow_lite API

[![Build Status](https://travis-ci.com/MRichardN/stackoverflow_lite_api.svg?branch=develop)](https://travis-ci.com/MRichardN/stackoverflow_lite_api)

The api enables you to ask questions




# Starting the application
Run the following commands inorder to set the environment and start the application respectively
```
export SECRET="input some random string"

export APP_SETTINGS="development"

export FLASK_APP=run.py

flask run
```

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