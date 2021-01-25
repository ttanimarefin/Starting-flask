from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

#replay  name
@app.route('/tune/<string:name>')
def tune(name):
    return "hello,"+name


@app.route('/users/<string:name>/<int:id>')
def user(name,id):
    return "hello," +name+ ", your id:" + str(id)


app.run(debug=True,port=8080)











