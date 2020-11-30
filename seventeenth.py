small_so_far = None
print('beginning', small_so_far)
for the_num in [8, 57, 14, 1, 88, 18] :
  if small_so_far is None :
    small_so_far = the_num
  elif the_num < small_so_far :
    small_so_far = the_num
  print(small_so_far, the_num)

print('fin!', small_so_far)
