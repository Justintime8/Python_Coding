import re
x = 'Sherry misses her funny inside jokes with strawberry head'
y = re.findall('h ([^ ]*)', x)
print(y)
