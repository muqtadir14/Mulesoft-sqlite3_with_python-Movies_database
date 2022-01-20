import sqlite3

conn = sqlite3.connect('Movies.db')
c = conn.cursor()

c.execute('''SELECT * FROM movies''')
print('\n -----All available movies----- \n')
print(c.fetchall())

c.execute('''SELECT * FROM movies WHERE LEAD_ACTOR='Aamir Khan' ''')
print('\n ------Movies in which lead actor is Aamir Khan------ \n')
print(c.fetchall())

c.execute('''SELECT * From movies where YEAR_OF_RELEASE=2009''')
print('\n -----Movies in the year 2009------- \n')
print(c.fetchall())
			 
#commit the changes to db			
conn.commit()
#close the connection
conn.close() 

