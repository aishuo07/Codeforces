n = int(input())
a= list(map(int, input().split()))
mini = 9999999
c = []
for i in range(len(a)):
    if mini>a[i]:
        mini = a[i]
        c = []
    if mini==a[i]:
        c.append(i)
if mini<n:
    b = max(c)
    d = []
    remaining = n-a[b]*(n//a[b])
    s = ""
    for i in range(n//a[b]):
        flag = True
        for j in range(8, b, -1):
            if a[j]-a[b]<=remaining:
                d.append(j+1)
                remaining-=a[j]-a[b]
                flag = False
                break
        if flag:
            d.append(b+1)
    print(''.join(str(x) for x in d))
else:
    print(-1)
