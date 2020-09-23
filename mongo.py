'''
How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?

It was very difficult to get my titanic.csv into a format readable by Postgres.
However, I like the pre-planned schema. It helped me think about my data more clearly.

MongoDB is intimidating because a typo can generate a new field, and I generate too many typos.

It seemed harder to get data ready for Postgres, however I didn't actually have to prepare the
data that went into MongoDB.























'''
from dotenv import load_dotenv
import json
import os
import pandas as pd
import pymongo
from pdb import set_trace as breakpoint
# from pymongo import MongoClient


# Load .env file and get credentials
load_dotenv()
MONGO_USER = os.getenv("MONGO_USER", default='OOPS')
MONGO_PW = os.getenv("MONGO_PW", default='OOPS')
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER", default='OOPS')

# client = pymongo.MongoClient("mongodb+srv://admin:<password>@cluster0.rqzzo.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db = client.test


connection_uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PW}@{MONGO_CLUSTER}?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_uri)
db = client.test

client = pymongo.MongoClient(connection_uri)

print("CLIENT:", type(client), client)
print("URI:", connection_uri)
print("Databases:", client.list_database_names())

# set db to analytics
analytics_db = client.sample_analytics
print(analytics_db.list_collection_names())

# Access a specific collection

transactions = analytics_db.transactions
# How many transactions? -1746
print(transactions.count_documents({}))

# How many customers have over 50 transactions? -892
print(transactions.count_documents({'transaction_count': {'$gt': 50}}))

# Get all customers into a dataframe
customers = analytics_db.customers
all_customers = customers.find()

df = pd.DataFrame(all_customers)

# Read JSON file 
with open('test_data_json.txt') as json_file:
    rpg_data = json.load(json_file)

# Create a rpg_data database
my_db = client.rpg_data

# Create a characters collection (empty) in the rpg_data DB
character_table = my_db.characters

#Insert the JSON data into the characters collection
character_table.insert_many(rpg_data)
print(character_table.count_documents({}))

