n, m = map(int, input().split())
c = []
for i in range(m):
    c.append(list(map(int, input().split())))
d={}
e = {'R':2, 'W':1, 'B':3}
for i in c:
    a = ['R','B','W']
    k = 0
    l = 0
    m = 0
    if i[0] in d:
        a.remove(d[i[0]])
        k = 1
    if i[1] in d:
        a.remove(d[i[1]])
        l = 1
    if i[2] in d:
        a.remove(d[i[2]])
        m = 1
    if len(a) != 0:
        if len(a) == 2:
            if k:
                d[i[1]] = a[0]
                d[i[2]] = a[1]
            elif l:
                d[i[0]] = a[0]
                d[i[2]] = a[1]
            else:
                d[i[0]] = a[0]
                d[i[1]] = a[1]
        if len(a) == 1:
            if k and l:
                d[i[2]] = a[0]
            elif l and m:
                d[i[0]] = a[0]
            else:
                d[i[1]] = a[0]
        if len(a) == 3:
            d[i[0]] = a[0]
            d[i[1]] = a[1]
            d[i[2]] = a[2]
a = [0]*(n)
for i in range(n):
    if (i+1) in d:
        a[i] = e[d[i+1]]
    else:
        a[i] = 1
print(*a)
