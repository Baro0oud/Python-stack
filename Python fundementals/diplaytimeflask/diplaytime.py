from flask import Flask,render_template,request
display=Flask(__name__)

@display.route("/")
def index():
    return render_template("index.html")


@display.route("/result",methods=['POST'])
def result():
    name=request.form['your_name']
    loction=request.form['location']
    language=request.form['language']
    comments=request.form['comment']
    return render_template("result.html",username=name,userlocatin=loction,userlanguage=language,usercomments=comments)


if __name__ =='__main__':
    display.run(debug=True)