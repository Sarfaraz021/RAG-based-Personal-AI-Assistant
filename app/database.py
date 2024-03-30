from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

client: Optional[AsyncIOMotorClient] = None
database_name = 'Dany'  # Replace with your actual database name


async def connect_to_mongo():
    global client
    # Replace with your actual MongoDB URI
    client = AsyncIOMotorClient(
        'mongodb://ahmedali:5GSjzJST52jMSqOe@ac-zcpibqp-shard-00-00.pk6vazf.mongodb.net:27017,ac-zcpibqp-shard-00-01.pk6vazf.mongodb.net:27017,ac-zcpibqp-shard-00-02.pk6vazf.mongodb.net:27017/?replicaSet=atlas-11opjq-shard-0&ssl=true&authSource=admin')


async def close_mongo_connection():
    if client is not None:
        client.close()


def get_user_collection():
    if client is not None:
        # Use the database_name variable as a string
        return client[database_name].users
    else:
        raise RuntimeError("Database client has not been initialized")
