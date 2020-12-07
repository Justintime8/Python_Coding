counts = dict()
print('Enter a line to entertain me: ')
line = input('')

words = line.split()

print('funny words:', words)

print('I better be counting something funny...')
for word in words :
  counts[word] = counts.get(word,0) + 1

print('This is a funny count', counts)
