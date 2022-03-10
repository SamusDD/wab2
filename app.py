from flask import Flask, redirect, url_for
wabapp = Flask(__name__)

data = {}

@wabapp.route('/')
def home():
    return redirect(url_for('redir'))

@wabapp.route('/redirect')
def redir():
    return "You have been successfully redirected"

if __name__ == '__main__':
    wabapp.run(debug=True, host='0.0.0.0')

