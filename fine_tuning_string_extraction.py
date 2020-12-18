import re

x = 'Sherry misses her funny inside jokes with strawberry head'
y = re.findall('\S+aw\S+', x)
print(y)

y = re.findall('with (\S+aw\S+)', x)
print(y)
