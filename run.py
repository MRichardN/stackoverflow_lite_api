
#run.py

import os

from app.__init__ import create_app

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app(config_name)

@app.route('/')
def index():
    return "Hello world"

 

if __name__ == '__main__':
    app.run()




