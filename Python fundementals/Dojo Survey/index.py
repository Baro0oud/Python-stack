from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        gender = request.form['gender']
        subscribe = request.form.get('subscribe', False)
        interests = request.form.getlist('interests')

        # Render result template with form data
        return render_template('result.html', name=name, email=email, age=age, gender=gender, subscribe=subscribe, interests=interests)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
