from flask import Flask,render_template
app = Flask(__name__)

#application routes
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
# RUN IN DEBUGGER MODE
# flask --app app run --debug
