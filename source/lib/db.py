from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from dotenv import dotenv_values
from pprint import pprint

 
class MongoDBConnectionManager: 
    def __init__(self): 
        self.hostname: str = str(dotenv_values('.env')['MONGODB_HOSTNAME'])
        self.port: int = int(dotenv_values('.env')['MONGODB_PORT'])
        self.connection = None
        print('✅ Open Connected With MongoDB...')

    def __enter__(self): 
        self.connection = MongoClient(self.hostname, self.port)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback): 
        if self.connection is not None:
            self.connection.close()
            print('❌ Close Connected With MongoDB...')
        else:
            print('❗️ ❗️ ❗️ MongoDB Connection Fault ❗️ ❗️ ❗️')


# CRUD
class EquipmentCRUD:
    def __init__(self):
        self.hostname: str = str(dotenv_values('.env')['MONGODB_HOSTNAME'])
        self.port: int = int(dotenv_values('.env')['MONGODB_PORT'])
        self.db = MongoClient(self.hostname, self.port)[str(dotenv_values('.env')['MONGODB_DB'])]
        self.collection = str(dotenv_values('.env')['MONGODB_COLLECTION'])

    def insert_data( self, equipment: dict) -> None:
        with MongoDBConnectionManager():
            self.db[self.collection].insert_one(equipment)
            print('🟢 Insert Data To MongoDB...')

    async def find_data(self, serial: dict):
            async with MongoDBConnectionManager():
                pprint(await self.db[self.collection].find({'lang':'Python'}))
                print('🔵 Find Data From MongoDB...')

    def update_data(self, serial_number: str, equipment: dict) -> None:
        with MongoDBConnectionManager():
            self.db[self.collection].update_one(serial_number, equipment)
            print('🟣 Update Data To MongoDB...')

    def delete_data(self, serial_number: str) -> None:
        with MongoDBConnectionManager():
            self.db[self.collection].delete_one(serial_number)
            print('🔴 Delete Data From MongoDB...')

EquipmentCRUD().find_data(serial = {'lang':'Python'})