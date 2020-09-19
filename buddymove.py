import pandas as pd 
import sqlite3

# df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')
# print(df.shape)

df = pd.read_csv('buddymove_holidayiq.csv', header=0, names = ['User_Id', 'Sports',
                 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic'])
print(df.shape)
print(df.describe())

df = df.applymap(lambda x: x.strip() if type(x) == str else x)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# df.to_sql('buddymove', con=conn, if_exists='replace')

cursor = conn.cursor()

results = cursor.execute('SELECT * FROM buddymove;').fetchall()
# print(results)

query1 = '''
--- How many rows? 
SELECT
    COUNT(User_Id)
FROM
	buddymove;
'''
result = cursor.execute(query1).fetchall()
print('Number of rows: \n',result)
	
query2 = '''
SELECT
	User_Id,
	Nature,
	Shopping
FROM buddymove
WHERE Nature >= 100 AND Shopping >= 100
LIMIT 5;
'''
result = cursor.execute(query2).fetchall()
print('Header list for top reviewers: \n', result)

query3 = '''
SELECT
	COUNT(User_Id)
FROM buddymove
WHERE Nature >= 100 AND Shopping >= 100;
'''
result = cursor.execute(query3).fetchall()
print('Number of users who reviewed 100+ Nature and 100+ Shopping: \n', result)



'''
python buddymove.py
'''