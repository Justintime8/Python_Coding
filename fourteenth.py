count = 0
sum = 0
print('beginning', count, sum)
for value in [8, 52, 14, 2, 74, 18] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('fin!', count, sum, sum / count)
