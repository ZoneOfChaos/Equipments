import motor.motor_asyncio
from dotenv import dotenv_values

client = motor.motor_asyncio.AsyncIOMotorClient(dotenv_values('.env')['CONNECTION_STRING'])
print('🚀 Connected to MongoDB...')
