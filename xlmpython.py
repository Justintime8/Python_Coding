import xml.etree.ElementTree as ET
data = '''<person>
  <name>Justin</name>
  <phone type="intl">
    773 202 5862
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
