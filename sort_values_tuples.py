c = {'sherry': 5, 'justin': 22, 'rae': 13}
mtv = list()
for k,v in c.items() :
  mtv.append((v,k))

print(mtv)

mtv = sorted(mtv,reverse=True)
print(mtv)
