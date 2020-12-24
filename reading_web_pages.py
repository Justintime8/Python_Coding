import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
l = list()
for line in fhand :
    line = line.decode()
    if not line.startswith('href=') :
        continue
    line = line.split()
    line = line[1]
    l.append(line)
    print(l)
