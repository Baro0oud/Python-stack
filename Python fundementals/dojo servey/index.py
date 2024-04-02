from flask import Flask , render_template , request
app=Flask(__name__)


@app.route("/")
def index1():
    return render_template("index.html")


@app.route("/results",methods=['POST'])
def index2():
    name=request.form['yourname']
    location=request.form['selections']
    language=request.form['selection-languages']
    area=request.form['comment']
    return render_template("results.html",username=name,loc=location,lan=language,comment=area)


if __name__=='__main__':
    app.run(debug=True)

