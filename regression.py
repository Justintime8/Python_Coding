import re
fh = open('regex_sum_1076677.txt')
hand = fh.read()
y = re.findall('[0-9]+', hand)
count = 0
sum = 0
for num in y:
    count = count + 1
    sum = sum + int(num)
    print(count,sum)
