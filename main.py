from flask import Flask, send_file

app=Flask(__name__)

@app.route("/")
def homeScreen():
    return "add /[status_code] to see what it does"

@app.route("/200")
def code200():
    filename="200statusCode.jpeg"
    return send_file(filename, mimetype='image')

if __name__=="__main__":
    app.run()