fname = input("Enter file name: ")
fh = open(fname)
fun = list()
for line in fh :
    words = line.rstrip().split()
    for shake in words:
        if shake in fun:
            continue
        else :
            fun.append(shake)
fun.sort()
print(fun)             
