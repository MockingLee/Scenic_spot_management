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
        return render_template("searchResult.html",dict = result )
    else:
        return render_template("searchFail.html")

@app.route('/rank',methods=['GET'])
def rank():
    initial.g.showGraph()
    result = initial.g.selectSort()
    print(result)
    return render_template("rankResult.html",dict = result)

@app.route('/map',methods=['GET'])
def map():
    nodeArr = []
    for i in initial.g.edgeinfo:
        nodeArr.append(i)
    return render_template("mapResult.html",mapArr = initial.g.getMatrix(),nodeArr = nodeArr,size = len(nodeArr))

@app.route('/delete',methods=['GET'])
def delete():
    name = request.args['name']
    result = initial.delete(name)
    if result:
        return render_template("success.html")
    else:
        return render_template("error.html")

@app.route('/insert',methods=['GET'])
def insert():
    name = request.args['name']
    description = request.args['description']
    popularity = request.args['popularity']
    rest_zone = request.args['rest_zone']
    toilet = request.args['toilet']
    if name is "" or description is "" or popularity is "" or rest_zone is "" or toilet is "":
        return render_template("error.html")
    if initial.insert(name,description,popularity,rest_zone,toilet):
        return render_template("insertSuccess.html",name = name)
    else:
        return render_template("error.html")

@app.route('/addEdge',methods=['GET'])
def addEdge():
    name = request.args['name']
    dest = request.args['dest']
    weight = request.args['weight']
    if initial.addEdge(name,dest,weight):
        return render_template("success.html")
    else:
        return render_template("error.html")

@app.route('/shortest',methods=['GET'])
def shortest():
    start = request.args['start']
    end = request.args['end']
    result = initial.getShortestPath(start,end)
    if result == -1:
        return render_template("error.html")
    else:
        return render_template("pathResult.html",dict = result)

@app.route('/route',methods=['GET'])
def route():
    start = request.args['name']
    result = initial.getRoute(start)
    if not result:
        return render_template("error.html")
    else:
        return render_template("routeResult.html", dict=result)

@app.route('/parking',methods = ['GET'])
def parking():
    return render_template("parking,html")

@app.route('/carIn',methods = ['GET'])
def carIn():
    initial.carIn(request.args['num'])
    return

@app.route('/carOut',methods = ['GET'])
def carOut():
    num = request()





if __name__ == '__main__':
    app.run()
