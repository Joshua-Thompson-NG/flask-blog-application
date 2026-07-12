from flask import Flask,render_template
app = Flask(__name__)


# dummy data for testing
posts = [
    {"author":"Oluwatomi Thompons",
    "title":"Why python is slow as fuck",
    "content":"Python is really slow, like really really slow and in this post I want to discuss why that is in detail. but firstly some context...",
    "date_posted":"July 12, 2026"},

    {"author":"Joseph Oke",
    "title":"My second post",
    "content":"second posting content",
    "date_posted":"July 13, 2026"},

    {"author":"Micheal Jackson",
    "title":"My first post here on my main account",
    "content":"what have I been up to lately?",
    "date_posted":"July 12, 2026"},
    
]



#application routes
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title='About')




if __name__ == "__main__":
    app.run(debug=True)
# RUN IN DEBUGGER MODE
# flask --app app run --debug
