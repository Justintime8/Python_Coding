import json
data = '''{
  "name" : "Justin",
  "phone" : {
    "type" : "intl",
    "number" : "1+ 773 202 5862"
    },
    "email" : {
    "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])
