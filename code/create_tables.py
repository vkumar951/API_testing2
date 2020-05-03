import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_table="CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY , username text , password text) "
cursor.execute(create_table)

create_table="CREATE TABLE IF NOT EXISTS ITEMS ( name text , price real) "
cursor.execute(create_table)

cursor.execute("INSERT INTO ITEMS VALUES ('test',10.99 )")

connection.commit()
connection.close()
