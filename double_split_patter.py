line = 'From Justintime@dpi.uc.mi Sun June 8 08:18:08 2020'
words = line.split()
print(words)
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[1])
