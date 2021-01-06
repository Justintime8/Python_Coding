import sqlite3
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)',
  ('One More Time', 26))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)',
  ('The Beautiful People', 8))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur :
  print(row)

cur.close()
