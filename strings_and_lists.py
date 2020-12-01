bao = 'Sherry likes her fried chicken spicy'
like = bao.split()
print(like)

print(len(like))

print(like[3:5])

print(like)

for s in like :
    print(s)


she = 'needs a lot of             heytea'
he = she.split()
print(he)

she = 'needs;lots;of;ramen'
him = she.split()
print(him)

print(len(him))

him = she.split(';')
print(him)
print(len(him))
