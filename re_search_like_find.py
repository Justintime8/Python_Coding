import re
hand = open('regex_sum_1076677.txt')
for line in hand :
  line = line.rstrip()
  if re.search('From:', line) :
    print(line)
