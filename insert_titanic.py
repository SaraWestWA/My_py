from dotenv import load_dotenv
import os
import pandas
import pymongo
import psycopg2
from psycopg2.extras import execute_values
from pdb import set_trace as breakpoint

# Load .env file and get credentials
load_dotenv()
DB_NAME = os.getenv("DB_NAME", default='OOPS')
DB_USER = os.getenv("DB_USER", default='OOPS')
DB_PASS = os.getenv("DB_PASS", default='OOPS')
DB_HOST = os.getenv("DB_HOST", default='OOPS')

# Connect to ElephantSQL-hosted PostgreSQL DB
conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST)

cursor = conn.cursor()
# conn.commit()

CSV_FILEPATH = 'titanic.csv'
# ################ Create Postgres Table and Add Titanic Data ################

create_titanic_query = '''
DROP TABLE IF EXISTS titanic;
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL PRIMARY KEY,
    survived BOOLEAN,
    pclass class,
    name TEXT,
    sex VARCHAR(6),
    age DECIMAL,
    siblings_spouses_aboard SMALLINT,
    parents_children_aboard SMALLINT,
    fare DECIMAL(7,4)
)
'''
cursor.execute(create_titanic_query)

# ################ Retrieve Titanic Data ################

df = pandas.read_csv(CSV_FILEPATH)
print(df.dtypes)

'''Postgres does not like int64 datatypes, among others. Converting
all data to strings makes it readable by postgres. Using the "big_query" method
from elephant_rpg_pipeline did not work. The spaces in the name field
created a syntax error from cursor.execute(query).
'''

df = df.applymap(str)
print(df.dtypes)

# ################ Insert Titanic Data in Postgres ################
tuple_list = list(df.to_records(index=False))

t_query = f'INSERT INTO titanic(survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard,fare)VALUES %s'

# # execute values because of so many variables?
execute_values(cursor, t_query, tuple_list)

conn.commit()
