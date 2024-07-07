from flask import Flask, send_file, render_template

app=Flask(__name__)

@app.route("/")
def homeScreen():
    return render_template("index.html")

@app.route("/200")
def code200():
    filename="images/200statusCode.jpeg"
    return send_file(filename, mimetype='image')

if __name__=="__main__":
    app.run()