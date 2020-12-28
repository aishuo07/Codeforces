n, m = map(int, input().split())
a= list(map(int, input().split()))
b = []
for i in a:
    if i<0:
        b.append(-1*i)
b.sort()
if len(b)<=m:
    print(sum(b))
else:
    print(sum(b[len(b)-(m):]))
