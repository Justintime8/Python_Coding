import json
input = '''[
  { "id" : "008",
    "x" : "22",
    "name" : "Justin"
  },
  { "id" : "005",
    "x" : "21",
    "name" : "Sherry"
  }
]'''

info = json.loads(input)
print('User count: ', len(info))
for item in info :
  print('Name: ', item["name"])
  print('Id: ', item["id"])
  print('Attribute: ', item["x"])
