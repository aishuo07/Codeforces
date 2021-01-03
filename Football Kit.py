c = []
d = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    c.append(x)
    d.append(y)
total = 2*(n-1)
dir = {}
for i in c:
    try:
        dir[i]+=1
    except:
        dir[i] = 1
for i in range(n):
    try:
        print(int(total/2+dir[d[i]]), int(total/2-dir[d[i]]))
    except:
        print(int(total/2), int(total/2))
