import re
x = 'My 3 favorite numbers are 22 and 5 and 13'
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[aeiou]+', x)
print(y)
