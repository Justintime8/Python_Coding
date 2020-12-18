import re
x = 'Sherry really enjoys her fried chicken three times a day'
y = re.findall('^S.+y',x)
print(y)
