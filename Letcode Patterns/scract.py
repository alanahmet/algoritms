b = "asdfasda"
a = {}
for i in b:a[i] = 1 if not a.get(i) else a[i] + 1
a["a"]-=3
print(b[0])
