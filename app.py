from fun import initial
from flask import *
from app import app


app = Flask(__name__)


@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/loginSub',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['pwd']
    if username == "admin" and password == "admin":
        return render_template("administer.html")
    else:
        return render_template("loginFail.html")

@app.route('/search',methods=['GET'])
def search():
    name = request.args['name']
    result = initial.search(name)
    if result:
        return render_template("searchResult.html",name = name,dict = result )
    else:
        return render_template("searchFail.html")

@app.route('/rank',methods=['GET'])
def rank():
    result = initial.g.selectSort()
    return render_template("rankResult.html",dict = result)


if __name__ == '__main__':
    app.run()
