from flask import Flask

# Exporting environmental variables eg
# export FLASK_APP=flask.py & export FLASK_ENV=development
# To run a flask app : flask run

app= Flask(__name__)

@app.route('/')

def index():
    return 'hello'

@app.route('/api/testimonials')
def testimonials():
    return {'testimonials':['great','its ok']}