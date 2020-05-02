import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_table="CREATE TABLE USERS (id int , username text , password text)"

cursor.execute(create_table)

user=(1,'vikas','vikas')
insert_query="INSERT INTO USERS VALUES (?,?,?)"
cursor.execute(insert_query,user)

connection.commit()
connection.close()
