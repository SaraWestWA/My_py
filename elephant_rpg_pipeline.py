import psycopg2

DB_NAME = 'clvpkepu'
DB_USER = 'clvpkepu'
DB_PASS = 'QiL-f_Trjqq9LWdIhSHB6m6eknAn0qXa'
DB_HOST = 'lallah.db.elephantsql.com'

# Connect to ElephanSQL - hosted ProstgreSQL DB
conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST)

cursor = conn.cursor()

cursor.execute('SELECT * from test_table;')

results = cursor.fetchall()
# print(results)


'''
python elephant_rpg_pipeline.py
'''

################ Connect to SQLite DB for RPG Data ################

import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cursor = sl_conn.cursor()
characters = sl_cursor.execute ('SELECT * FROM charactercreator_character;').fetchall()
# print(characters)

################ Create the Character Table in Postgres and Insert Data ################
create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT, 
    intelligence INT,
    dexterity INT,
    wisdom INT
)
'''
cursor.execute(create_character_table_query)
conn.commit()

# ### okay to use below for small data tables"
# for character in characters:
#     insert_query = f'''INSERT INTO rpg_characters
#     (character_id, name, level, exp, hp, strength,
#      intelligence, dexterity, wisdom) VALUES
#     {character}
#     '''
#     cursor.execute(insert_query)
# conn.commit()

### much faster for larger groups of data
big_query = '''INSERT INTO rpg_characters
    (character_id, name, level, exp, hp, strength,
     intelligence, dexterity, wisdom) VALUES'''
for character in characters:
    big_query += f' {character},'

# Replace trailing ',' with a ';'
big_query = big_query.rstrip(',') + ';'   

cursor.execute(big_query)
# conn.commit()

#####Create the armory_items Table in Postgres and Insert Data#####
items = sl_cursor.execute ('SELECT * FROM armory_item;').fetchall()

create_item_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_armory_items (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    "value" INT NOT NULL,
    weight INT NOT NULL
)
'''

cursor.execute(create_item_table_query)
conn.commit()

##### Fill armory_item Table with Data #####
item_query = ''' INSERT INTO rpg_armory_items
    (item_id, name, "value", weight) VALUES'''
for item in items:
        item_query += f' {item},'

# print(item_query)

cursor.execute(item_query)

conn.commit()

# conn(close)
