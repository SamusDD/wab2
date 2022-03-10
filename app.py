from flask import Flask, redirect, url_for

data = {}
i = 0

wabapp = Flask(__name__)

@wabapp.route('/')
def home():
    return data

@wabapp.route('/create/<message>')
def create(message):
    global i
    data[i] = message
    i += 1
    return message + " added to dictionary"

@wabapp.route('/update/<int:i>')
def update(i, newmessage):
    data[i] = newmessage
    return "Updated entry"

@wabapp.route('/delete/<int:i>')
def delete(i):
    data.pop(i)
    return "Deleted entry"

if __name__ == '__main__':
    wabapp.run(debug=True, host='0.0.0.0')

