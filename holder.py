import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas
load_dotenv() #> loads contents of the .env file into the script's environment
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASS = os.getenv("DB_PASS", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")
CSV_FILEPATH = "titanic.csv"
#CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
#CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module2-sql-for-analysis", "titanic.csv")
#
# CONNECT TO THE PG DATABASE
#
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>
cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>
#
# CREATE A TABLE TO STORE THE PASSENGERS
#
# ... optionally renaming some of the columns, adding a primary key, and changing survived to a bool
sql = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived boolean,
    pclass int4,
    full_name text,
    gender text,
    age int4,
    sib_spouse_count int4,
    parent_child_count int4,
    fare float8
);
"""
cursor.execute(sql)
#
# READ PASSENGER DATA FROM THE CSV FILE
#
df = pandas.read_csv(CSV_FILEPATH)
print(df.columns.tolist())
print(df.dtypes)
print(df.head())


DROP TABLE IF EXISTS titanic;
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL PRIMARY KEY,
    survived BOOLEAN,
    pclass class,
    name TEXT,
    sex VARCHAR(6),
    age SMALLINT,
    siblings_spouses_aboard SMALLINT,
    parents_children_aboard SMALLINT,
    fare DECIMAL(7,4)
)

#
# INSERT DATA INTO THE PASSENGERS TABLE
#
# how to convert dataframe to a list of tuples?
list_of_tuples = list(df.to_records(index=False))
insertion_query = f"INSERT INTO passengers (survived, pclass, full_name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples) # third param: data as a list of tuples!
# CLEAN UP
connection.commit() # actually save the records / run the transaction to insert rows
cursor.close()
connection.close()

import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
with open('user_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s)",
        row
    )
conn.commit()

# SHORT, TIDY WAY! That won't work for me
# with open('titanic.csv', 'r') as passengers:
#     next(passengers) #skips header row
#     cursor.copy_from(passengers)



# passengers = open('titanic.csv', 'r')
# lines = passengers.readlines()[1:]




    # (Survived, Pclass, Name, sex, age,
    # siblings_spouses_aboard, parents_children_aboard,
    # fare) VALUES'''

 
# ################ Retrieve Titanic Data ################
with open('titanic.csv', 'r') as passengers:
    reader = csv.reader(passengers, delimiter=',', quotechar="|")
    next(reader) # Skip the header row.
    for row in reader:
        t-query
        '''INSERT INTO titanic VALUES
        (survived, pclass, name, sex, age,
        siblings_spouses_aboard, parents_children_aboard,
        fare)''',
        row
        )

        # with open('titanic.csv', 'r') as passengers:
#     passengers = csv.reader(passengers, delimiter=' ', quotechar="|")
#     next(passengers) # Skip the header row.
#     for person in passengers:
        
#         person
# with open('titanic.csv' , 'r') as passengers:
#     first_line = passengers.readline()


# Replace trailing ',' with a ';'
# t_query = t_query.rstrip(',') + ';'



# ################ Retrieve Titanic Data ################

# t_query = '''INSERT INTO titanic VALUES
#         (survived, pclass, name, sex, age,
#     # siblings_spouses_aboard, parents_children_aboard,
#     # fare)'''


conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("""CREATE TABLE users(
    id integer PRIMARY KEY,
    email text,
    name text,
    address text
)
""")
conn.commit()

import csv
>>> with open('eggs.csv', newline='') as csvfile:
...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print(', '.join(row))
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam

import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
with open('user_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s)",
        row
    )
conn.commit()
, delimiter=',', quotechar="|"