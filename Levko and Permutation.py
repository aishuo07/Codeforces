n, k = map(int, input().split())

if n == k:
    print(-1)
elif k == 0:
    p = 0
    l =[]
    for i in range(1, n+1):
        if p%2==0:
            l.append(i+1)
        else:
            l.append(i-1)
        if i == n and l[i-1] == n+1:
            l[n-1]-=1
            l[0], l[n-1] = l[n-1], l[0]
        p+=1
    print(*l)
else:
    l = []
    for i in range(1,k+2):
        l.append(i)
    t = 0
    for i in range(k+2, n+1):
        if t%2==0:
            l.append(i+1)
        else:
            l.append(i-1)
        if i == n and l[i-1] == n+1:
            l[n-1]-=1
            l[0], l[n-1] = l[n-1], l[0]
        t+=1
    print(*l)
