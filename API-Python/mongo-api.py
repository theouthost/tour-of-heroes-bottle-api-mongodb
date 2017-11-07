from bottle import Bottle, request, response, run, route, get, put, post, delete
import json
from bson import json_util
from bson.json_util import dumps

#Mongo Stuff
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')



#Access-Control-Allow-Origin

def allow_cors(func):
    """ this is a decorator which enable CORS for specified endpoint """
    def wrapper(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000' # * in case you want to be accessed via any website
        response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, application/json'
        return func(*args, **kwargs)

    return wrapper




@route("/")
def hello():
    return "Nothing Here!"

@route("/allheroes")
@allow_cors
def allheroes():
    db = client.heroes
    heroes = db.heronames
    data = dumps(heroes.find({}, {'_id': False}))
    return '{"data": '+data+'}'



@route("/update/<id:int>", method=['PUT', 'OPTIONS'])
@allow_cors
def update(id):    
    if request.method == 'OPTIONS':
        return {}
    else:
        data = request.body.read()
	data = json.loads(data)
	uname = data["name"]
	db = client.heroes
	heroes = db.heronames
	heroes.update_one(
	        {"id": id },
	        {"$set": { "name": uname }
	        }
	)
    return '{"status": "ok"}'


@route("/add", method=['POST', 'OPTIONS'])
@allow_cors
def add():    
    if request.method == 'OPTIONS':
        return {}
    else:
        data = request.body.read()
	data = json.loads(data)
	uname = data["name"]
	db = client.heroes
	heroes = db.heronames
        #Gunna Need to find the highest id number and add one to create an id.
        highestid = heroes.find_one({}, {'id': 1, '_id': 0}, sort=[("id", -1)])
	uid = highestid["id"]
	id = int(uid) + 1
	heroes.insert_one( {"id": id, "name": uname} )
        jsontoreturn = '{"data": {"id": ' + str(id) + ', "name": "' + uname + '"} }'
    return jsontoreturn




@route("/delete/<id:int>", method=['DELETE', 'OPTIONS'])
@allow_cors
def delete(id):    
    if request.method == 'OPTIONS':
        return {}
    else:
	db = client.heroes
	heroes = db.heronames
	heroes.delete_one({"id": id })
    return '{"status": "ok"}'







run(host='localhost', port=8080, debug=True)
