n, m = map(int, input().split())
if n == 1:
    print((m+1)//2)
else:
    c = []
    j = 0
    res = []
    if m%2==0:
        l = (m+1)//2
        r = l+1
    else:
        c.append((m+1)//2)
        l = (m+1)//2-1
        r = (m+1)//2+1
    for i in range(m//2):
        c.append(l-i)
        c.append(r+i)
    for i in range(n//m):
        res+=c
    res+=c[:n%m]
    for i in res:
        print(i)
