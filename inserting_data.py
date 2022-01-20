import sqlite3

conn = sqlite3.connect('Movies.db')
c = conn.cursor()

#list of movies
play_list = [('Dangal', 'Aamir Khan', 'Sakshi Tanwar', 2016, 'Nitesh Tiwari'),
		   ('The Lunchbox', 'Irrfan Khan', 'Nimrat Kaur', 2013, 'Ritesh Batra'),
		   ('3 Idiots', 'Aamir Khan', 'Kareena Kapoor', 2009, 'Rajkumar Hirani'),
           ('Krrish', 'Hrithik Roshan', 'Priyanka Chopra', 2006, 'Rakesh Roshan'),
           ('Happy New Year', 'Shah Rukh Khan', 'Deepika Padukone', 2014, 'Farah Khan'),
           ('Lagaan', 'Aamir Khan', 'Gracy Singh', 2001, 'Ashutosh Gowariker')]

#insert multiple movies at a time
c.executemany('INSERT INTO movies VALUES(?,?,?,?,?);',play_list);

print('Movies registered =', c.rowcount)

#commit the changes to db			
conn.commit()
#close the connection
conn.close() 
