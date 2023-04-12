import pymongo
from flask import Flask
from pymongo import MongoClient

# "mongodb+srv://medo00001:KdOY93oz1MmMAfMN@cluster0.1k8ou.mongodb.net/test"

connection_to = MongoClient(
    "mongodb+srv://medo00001:KdOY93oz1MmMAfMN@cluster0.1k8ou.mongodb.net/test"
)

# make data base manual and add collection
# dbs = cluster.list_database_names()
# print(dbs)  ['test_db', 'admin', 'local']
# collections = my_db_connect.list_collection_names()
# print(collections)   ['etender_collection']

my_db_connect = connection_to.test_db

def insert_document(document):
    my_db_connect.etender_collection.insert_one(document)
    
