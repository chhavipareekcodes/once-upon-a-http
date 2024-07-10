from flask import Flask, send_file, render_template

app=Flask(__name__)

@app.route("/")
def homeScreen():
    return render_template("index.html")

@app.route("/200")
def code200():
    filename="images/200statusCode.jpeg"
    return [send_file(filename, mimetype='image')]

@app.route("/102")
def code102():
    filename="images/102statusCode.jpeg"
    return [send_file(filename, mimetype='image')]

@app.route("/202")
def code202():
    filename="images/202statusCode.jpeg"
    return [send_file(filename, mimetype='image')]

@app.route("/208")
def code208():
    filename="images/208statusCode.jpeg"
    return [send_file(filename, mimetype='image')]

@app.route("/300")
def code300():
    filename="images/300statusCode.jpeg"
    return [send_file(filename, mimetype='image')]


if __name__=="__main__":
    app.run()