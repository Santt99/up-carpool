from flask import Flask
from DB import DB
from json import dumps
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    db = DB("mongodb://{}:{}@ds159328.mlab.com:59328/heroku_4g6p2nzn".format("front", "Teclado12M"))
    visit_id = db.register_visit()
    response = dumps({"visitId": str(visit_id)})
    print(response)
    return response

@app.route('/updatevisit/<id>/<email>')
def update_visit(id, email):
    from datetime import datetime
    db = DB("mongodb://{}:{}@ds159328.mlab.com:59328/heroku_4g6p2nzn".format("front", "Teclado12M"))
    data = {"$set": {"second_timestamp": datetime.now(), "email": email}}
    key = {"_id": ObjectId(id)}
    db.update_visit(key, data)
    return dumps({"message": "Succesfully updated visit"})

if __name__ == '__main__':
    app.run()