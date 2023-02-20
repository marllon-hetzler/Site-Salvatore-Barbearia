from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

if __main__ == __name__:
    app.run(debug=True)