from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name.capitalize()}!'

@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return word * num

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."

if __name__ == '__main__':
    app.run(debug=True)
