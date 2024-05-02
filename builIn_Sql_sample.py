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
#additional 1 
rows = cursor.fetchall()

# print 
for row in rows:
   print (row) 
#addition 2 
#updating table

cursor.execute( " UPDATE users SET age = ? WHERE name = ? ", (29, Kim) )
conn.commit()
print ( "\nUPDATEd Kim's age.")

# retriving after updates 
cursor.execute( "SELECT * FROM USERS")
updated_rows = cursor.fetchall()

#print updated info 
print ("\nData in the table after updating: ")
for row in updated_rows:
  print(row) 
  
#closing connection 
conn.close()
