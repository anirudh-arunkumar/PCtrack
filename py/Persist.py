import pymongo
from pymongo import MongoClient


class Persist:
    def __init__(self, hostname=None, port=None):
        if hostname is None:
            self._host = "192.168.1.247"
        else :
            self._host = hostname

        if port is None:
            self._port = 27017
        else:
            self._port = port

        self._client = MongoClient(self._host, self._port)
        self._db = self._client.itrackerdb
        self._product_list_coll = self._db["pricelist"]
        #print(self._db.list_collection_names())

    def save_products(self, datas):
        self._product_list_coll.insert_many(datas)

    def save_product(self, data):
        self._product_list_coll.insert_one(data)
