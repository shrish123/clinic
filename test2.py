import sqlite3
 
conn = sqlite3.connect("mydata.db") 
 
cursor = conn.cursor()
 

cursor.execute("""CREATE TABLE grp
                  (name text, age integer,timing integer) 
               """)
