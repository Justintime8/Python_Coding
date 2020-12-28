import xml.etree.ElementTree as ET
input = '''<stuff>
  <users>
    <user x ="2">
      <id>008</id>
      <name>Justin</name>
    </user>
    <user x="7">
      <id>005</id>
      <name>Sherry</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst :
  print('Name: ',item.find('name').text)
  print('Id: ', item.find('id').text)
  print('Attribute: ', item.get("x"))
  
