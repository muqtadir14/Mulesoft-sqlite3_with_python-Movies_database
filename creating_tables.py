import sqlite3

conn = sqlite3.connect('Movies.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE movies(
                                MOVIE_NAME TEXT NOT NULL,
                                LEAD_ACTOR TEXT NOT NULL,
                                LEAD_ACTRESS TEXT NOT NULL,
                                YEAR_OF_RELEASE INTEGER NOT NULL,
                                DIRECTOR TEXT NOT NULL)''')
			
#commit the changes to db			
conn.commit()
#close the connection
conn.close() 