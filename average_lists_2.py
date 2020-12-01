numlist = list()
while True :
  inp = input('Give me your number: ')
  if inp == 'done' : break
  value = float(inp)
  numlist.append(value)

average = sum(numlist)/len(numlist)
print('average', average)
