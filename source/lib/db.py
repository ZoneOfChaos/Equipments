from pymongo import MongoClient
from dotenv import dotenv_values

# read .env file
hostname = dotenv_values('.env')['MONGODB_HOSTNAME']
port = int(dotenv_values('.env')['MONGODB_PORT'])
db = dotenv_values('.env')['MONGODB_DB']
collection = dotenv_values('.env')['MONGODB_COLLECTION']

class MongoDBConnectionManager(): 
    def __init__(self, hostname, port): 
        self.hostname = hostname 
        self.port = port 
        self.connection = None
  
    def __enter__(self): 
        self.connection = MongoClient(self.hostname, self.port) 
        return self
  
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.connection.close() 
  
# connect to MongoDB
with MongoDBConnectionManager(hostname, port) as mongo:
    collection_string = f'mongo.connection.{db}.{collection}' 
    collection = collection_string
    print('🚀 Connected to MongoDB...')
