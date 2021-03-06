import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
print(conn)

cursor = conn.cursor()
dir(cursor)


query1 = '''
-- Find total number of characters = 302
SELECT
    COUNT(DISTINCT character_id)
    FROM charactercreator_character;
'''
result = cursor.execute(query1).fetchall()
print('Total number of characters:', result)

query2 = '''
-- Find total number of Mage = 108
SELECT
    COUNT(character_ptr_id)
FROM charactercreator_mage;
'''
result = cursor.execute(query2).fetchall()
print('Total number mage:', result)


query3 = '''
-- Find total number of Necromancers, subset of Mage = 11
SELECT
	COUNT(mage_ptr_id)
FROM charactercreator_necromancer;
'''
result = cursor.execute(query3).fetchall()
print('Total number Mage as Necormancer:', result)


query4 = '''
-- Find total number of Thieves = 51
SELECT
	COUNT(character_ptr_id)
FROM charactercreator_thief;
'''
result = cursor.execute(query4).fetchall()
print('Total number Thieves:', result)


query5 = '''
-- Find total number of Clerics = 75
SELECT
	COUNT(character_ptr_id)
FROM charactercreator_cleric;
'''
result = cursor.execute(query5).fetchall()
print('Total number Clerics:', result)

query6 = '''
-- Find total number of Fighters = 68
SELECT
	COUNT(character_ptr_id)
FROM charactercreator_fighter;
'''
result = cursor.execute(query6).fetchall()
print('Total number Fighters:', result)

# query23456 = '''
# SELECT
# 	COUNT(DISTINCT charactercreator_mage.character_ptr_id) as mage,
# 	COUNT(DISTINCT charactercreator_necromancer.mage_ptr_id) as mage_necromancer,
# 	COUNT(DISTINCT charactercreator_thief.character_ptr_id) as thief,
# 	COUNT(DISTINCT charactercreator_cleric.character_ptr_id) as cleric,
# 	COUNT(DISTINCT charactercreator_fighter.character_ptr_id) as fighter
# FROM
# 	charactercreator_mage,
# 	charactercreator_necromancer,
# 	charactercreator_thief,
# 	charactercreator_cleric,
# 	charactercreator_fighter;
# '''
# result = cursor.execute(query23456).fetchall()
# print('Characters:', result)

query7 = '''
-- Find total number of items = 174
SELECT
	COUNT(item_id)
FROM
	armory_item;
'''
result = cursor.execute(query7).fetchall()
print('Total number Items:', result)


query8 = '''
-- Find total number of weapons = 37
SELECT
	COUNT(item_ptr_id)
FROM
	armory_weapon;
'''
result = cursor.execute(query8).fetchall()
print('Total number Weapons:', result)

'''-- Total non-weapon items = 174 -37 = 137
'''
'''COME BACK TO THIS COME BACK TO THIS, COME BACK TO THIS, COMEBACK TO THIS
print('Total number of Non-weapon Items: ' = query7-query8)
'''

query9 = '''
-- How many items does each character have?
SELECT
	inv.character_id,
	char.name,
	COUNT(inv.item_id) as NumItems
FROM
	charactercreator_character AS char
LEFT JOIN
	charactercreator_character_inventory AS inv
ON inv.character_id = char.character_id
GROUP BY char.character_id
LIMIT 20;
'''
result = cursor.execute(query9).fetchall()
print('Number of Items per Character: \n', result)
# item_df = pd.DataFrame(data=result, columns=['Char ID', 'Name', 'Num Items'])
# print (item_df)

query10 = '''
-- How many weapons does each chacter have?
SELECT
	char.character_id,
	char.name,
	COUNT(wep.item_ptr_id) as NumWeapons
FROM charactercreator_character_inventory as inv
LEFT JOIN armory_weapon as wep
ON inv.item_id = wep.item_ptr_id
LEft JOIN charactercreator_character AS char
ON inv.character_id = char.character_id
GROUP BY inv.character_id
LIMIT 20;
'''
result = cursor.execute(query10).fetchall()
print('Number of Weapons per Character: \n', result)


query11 = '''
-- On average how many items does each character have?
SELECT AVG(NumItems)
FROM (
	SELECT
		character_id,
		COUNT(item_id) as NumItems
	FROM
		charactercreator_character_inventory
	GROUP BY character_id
)
'''
result = cursor.execute(query11).fetchall()
print('Average number of Items:', result)


query12 = '''
-- On average how many weapons does each character have?
SELECT AVG(NumWeapons)
FROM (
	SELECT
		inv.character_id,
		inv.item_id,
		wep.item_ptr_id,
		COUNT(wep.item_ptr_id) as NumWeapons
    FROM charactercreator_character_inventory as inv
    LEFT JOIN armory_weapon as wep
    ON inv.item_id = wep.item_ptr_id
    GROUP BY inv.character_id
)
'''
result = cursor.execute(query12).fetchall()
print('Average number of Weapons:', result)

conn.close()
