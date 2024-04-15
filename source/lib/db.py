from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from dotenv import dotenv_values

# read .env file
hostname = dotenv_values('.env')['MONGODB_HOSTNAME']
port = int(dotenv_values('.env')['MONGODB_PORT'])
db_name = dotenv_values('.env')['MONGODB_DB']
collection_name = dotenv_values('.env')['MONGODB_COLLECTION']

class MongoDBConnectionManager: 
    def __init__(self, hostname: str, port: int): 
        self.hostname: str = hostname
        self.port: int = port 
        self.connection = None
        print('✅ Open Connected With MongoDB...')

    def __enter__(self): 
        self.connection = MongoClient(self.hostname, self.port) 
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.connection.close()
        print('❌ Close Connected With MongoDB...')      


# CRUD
class MongoDBCRUD:

    def insert_data( equipment: dict):
        with MongoDBConnectionManager(hostname, port):
            db = MongoClient(hostname, port)[db_name]
            db[collection_name].insert_one(equipment)
            print('🟢 Insert Data To MongoDB...')

    def find_data(serial_number: str):
        with MongoDBConnectionManager(hostname, port):
            db = MongoClient(hostname, port)[db_name]
            db[collection_name].find_one(serial_number)
            print('🔵 Find Data From MongoDB...')

    def update_data(serial_number, equipment):
        with MongoDBConnectionManager(hostname, port):
            db = MongoClient(hostname, port)[db_name]
            db[collection_name].update_one(serial_number, equipment)
            print('🟣 Update Data To MongoDB...')

    def delete_data(serial_number):
        with MongoDBConnectionManager(hostname, port):
            db = MongoClient(hostname, port)[db_name]
            db[collection_name].delete_one(serial_number)
            print('🔴 Delete Data From MongoDB...')