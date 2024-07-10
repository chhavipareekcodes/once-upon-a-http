from flask import Flask, send_file, render_template

app=Flask(__name__)

@app.route("/")
def homeScreen():
    return render_template("index.html")

@app.route("/<code>")
def satusCode(code):
    filename=f"images/{code}statusCode.jpeg"
    return send_file(filename, mimetype='image/jpeg')


if __name__=="__main__":
    app.run()