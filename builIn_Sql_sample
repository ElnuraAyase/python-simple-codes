# interacting with SQL lite 
import sqlite3

# connect to database
conn = sqlite3.connect('some.db')

#need a cursor 
cursor = conn.cursor()

#creating table 
cursor.execute( ''' CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER) ''' ) 

#add info

cursor.execute( "INSER INTO users (name, age) VALUES(?, ?) ", (Zhenya, 24))
cursor.execute( "INSER INTO users (name, age) VALUES(?, ?) ", (Kim, 29))
cursor.execute( "INSER INTO users (name, age) VALUES(?, ?) ", (Joo, 27))

#commint
conn.commit()

# data retrieve 

cursor.execute( "SELECT * FROM users" ) 

# print 
for in rows:
print (row) 

#closing connection 
conn.close()
