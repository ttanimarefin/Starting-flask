from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///posts.db'
db=SQLAlchemy(app)


all_posts = [
    {
        'title':'Post 1',
        'content' : 'This is the content of  post1',
        'author':'Tanim'
    },
    {
        'title':'Post 2',
        'content' : 'This is the content of  post2',
        
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
@app.route('/')
def posts():
    return render_template('posts.html',posts=all_posts)

#replay  name
@app.route('/tune/<string:name>')
def tune(name):
    return "hello,"+name


@app.route('/users/<string:name>/<int:id>')
def user(name,id):
    return "hello," +name+ ", your id:" + str(id)


app.run(debug=True,port=8080)











