from flask import Flask,render_template

app = Flask(__name__)

posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'content':'Blog Post 2',
    },

    {
        'author':'John Doe',
        'title':'Blog Post 2',
        'content':'Blog Post 3',
    },

    {
        'author':'Mike',
        'title':'Blog Post 3',
        'content':'Blog Post 4',
    }
]
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template("home.html",posts=posts)

@app.route('/about')
def about():
    return render_template("about.html",title="About")


if __name__ == '__main__':
    app.run(debug=True)