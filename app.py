from flask import Flask, render_template, make_response, request
from DB import DB
from json import dumps
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)

CORS(app)
DB_URL = "mongodb://{}:{}@ds159328.mlab.com:59328/heroku_4g6p2nzn".format("front", "Teclado12M")


@app.route('/')
def index():
    res = make_response(render_template("index.html"))
    if not request.cookies.get('visitId'):
        db = DB(DB_URL)
        visit_id = db.register_visit()
        res.set_cookie('visitId', str(visit_id))
    return res

@app.route('/index.js')
def get_index_js():
    print("Hi")
    return app.send_static_file("/templates/index.js")


@app.route('/updatevisit/<email>')
def update_visit(id, email):
    from datetime import datetime
    db = DB(DB_URL)
    data = {"$set": {"second_timestamp": datetime.now(), "email": email}}
    key = {"_id": request.cookies.get('visitId')}
    db.update_visit(key, data)
    return dumps({"message": "Succesfully updated visit"})

if __name__ == '__main__':
    app.run()