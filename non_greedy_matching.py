import re
x = 'Sherry really likes eating jian bing'
y = re.findall('^S.+?y', x)
print(y)
