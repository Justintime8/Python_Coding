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
