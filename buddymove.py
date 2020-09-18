import pandas as pd 
import sqlite3

df = read_csv('buddymove_holiday.csv')
print(df.shape)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

df.to_sql('buddymove', con=conn, if _exists='replace')

cursor = conn.cursor()

cursor.execute('SELECT * FROM buddymove;').fetchall()
'''
python buddymove.py
'''