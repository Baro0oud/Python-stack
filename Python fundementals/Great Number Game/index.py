from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def generate_random_number():
    return random.randint(1, 100)

def reset_game():
    session['random_number'] = generate_random_number()
    session['attempts'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'random_number' not in session:
        reset_game()
    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1
        if guess == session['random_number']:
            return redirect(url_for('winner'))
        elif session['attempts'] >= 5:
            return redirect(url_for('loser'))
        elif guess < session['random_number']:
            return render_template('index.html', message="Too low!")
        else:
            return render_template('index.html', message="Too high!")
    return render_template('index.html')

@app.route('/winner', methods=['GET', 'POST'])
def winner():
    if request.method == 'POST':
        session.pop('random_number')
        return redirect(url_for('index'))
    return render_template('winner.html', attempts=session['attempts'])

@app.route('/loser', methods=['GET', 'POST'])
def loser():
    if request.method == 'POST':
        session.pop('random_number')
        return redirect(url_for('index'))
    return render_template('loser.html')

if __name__ == '__main__':
    app.run(debug=True)
