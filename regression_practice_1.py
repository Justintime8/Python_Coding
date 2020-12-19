import re
x = 'Justin needs to study python as much as possible until 11:00 PM'
y = re.findall('l ([0-9]+.[0-9]+)', x)
print(y)
