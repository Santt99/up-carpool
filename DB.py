from pymongo import MongoClient


class DB(object):
    def __init__(self, url):
        self.__connection = MongoClient(url, retrywrites=False)
        self.__db = self.__connection["heroku_4g6p2nzn"]

    def register_visit(self):
        visits_collection = self.__db["visits"]
        from datetime import datetime

        res = visits_collection.insert({"first_timestamp": datetime.now(), "email": ""})
        return res

    def update_visit(self, key, data):
        visits_collection = self.__db["visits"]
        res = visits_collection.update_one(key, data)
        print(res)
