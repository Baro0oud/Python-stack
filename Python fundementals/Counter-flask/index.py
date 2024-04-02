from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/')
def index():
    # Initialize session variable if it doesn't exist
    session['count'] = session.get('count', 0)
    # Increment the count of visits
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/destroy_session')
def destroy_session():
    # Clear the session
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
