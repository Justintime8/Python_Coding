#Sherry loves Justin very much when he gives her french fries
data = 'Sherry loves Justin very much when he gives her french fries'
atpos = data.find('J')
print(atpos)
21
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)
