from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard_8x8():
    return render_template('checkerboard.html', rows=8, cols=8)

@app.route('/<int:x>')
def checkerboard_custom_rows(x):
    return render_template('checkerboard.html', rows=x, cols=8)

@app.route('/<int:x>/<int:y>')
def checkerboard_custom_size(x, y):
    return render_template('checkerboard.html', rows=x, cols=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboard_custom_colors(x, y, color1, color2):
    return render_template('checkerboard.html', rows=x, cols=y, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)
