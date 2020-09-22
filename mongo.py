from dotenv import load_dotenv
import os
import pandas
import pymongo
import psycopg2
from pdb import set_trace as breakpoint


# Load .env file and get credentials
load_dotenv()
MONGO_USER = os.getenv("MONGO_USER", default='OOPS')
MONGO_PW = os.getenv("MONGO_PW", default='OOPS')
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER", default='OOPS')


uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PW}@{MONGO_CLUSTER}?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
# db = client.test
print('URI:' , uri)

breakpoint()
