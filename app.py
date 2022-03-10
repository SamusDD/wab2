from flask import Flask

wabapp = Flask(__name__)

@wabapp.route('/')
def home():
    return "Hello Internet!"

if __name__ == '__main__':
    wabapp.run(debug=True, host='0.0.0.0')

