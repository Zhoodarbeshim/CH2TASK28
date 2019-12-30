a = [0, 1, 2, -4, -5, -6]
for i in a:
    if int(i) > 0:
        x = a.index(i)
        a[x] = 1
    elif int(i) < 0:
        x = a.index(i)
        a[x] = -1
print(a)