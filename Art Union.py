n, m = map(int, input().split())
c = []
for i in range(n):
    c.append(list(map(int, input().split())))
sumi = 0
print(c)
r = [0]*n
for i in range(n):
    if i ==0:
        sumi = sum(c[i])
        r[i] = sumi
    else:
        if c[i-1][m-1]>=sum(c[i][:m-1]):
            sumi+=c[i][m-1]
            r[i] = sumi
        else:
            sumi+=sum(c[i])-c[i-1][m-1]
            r[i] = sumi
print(*r)
    
