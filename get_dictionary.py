counts = dict()
names = ['sherry', 'justin', 'karen', 'sherry', 'sherry', 'jerry']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)
