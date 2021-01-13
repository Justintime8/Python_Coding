import sqlite3

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM People')
count = 0
print('People: ')
for row in cur :
    if count < 5: print(row)
    count = count + 1
print(count, 'rows.')

cur.execute('SELECT * FROM Follows')
count = 0
print('Follows: ')
for row in cur :
    if count< 5 : print(row)
    count = count + 1
print(count, 'rows.')

cur.close()
