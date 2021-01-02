import urllib.request as ur
import json

while True :
    address = input('Enter Location: ')
    print('Retrieving: ', address)
    uh = ur.urlopen(address)
    data = uh.read().decode()
    print('Retrieved: ', len(data), 'characters')
    js = json.loads(data)

    count = 0
    sum = 0

    for comment in js["comments"]:
        sum += int(comment["count"])
        count += 1
    print("Count:",count)
    print("Sum:",sum)
