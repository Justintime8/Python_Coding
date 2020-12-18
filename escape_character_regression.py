import re
x = 'Justin needs to spend $25.00 for Korean fried chicken.'
y = re.findall('\$[0-9.]+', x)
print(y)
