fname = input("Enter file name: ")
fh = open(fname)
if len(fname) < 1 : fname = "mbox-short.txt"
count = 0
for line in fh :
    	line = line.rstrip()
    	if line == "" : continue
        words = line.split()
        if words[0] !="From" : continue
        print(words[1])
        count = count + 1
