from pymongo import MongoClient


MONGO_URI = "mongodb://ahmedali:5GSjzJST52jMSqOe@ac-zcpibqp-shard-00-00.pk6vazf.mongodb.net:27017,ac-zcpibqp-shard-00-01.pk6vazf.mongodb.net:27017,ac-zcpibqp-shard-00-02.pk6vazf.mongodb.net:27017/?replicaSet=atlas-11opjq-shard-0&ssl=true&authSource=admin"
conn = MongoClient(MONGO_URI)
