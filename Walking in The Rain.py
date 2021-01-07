n, m = map(int, input().split())
c= []
for i in range(n):
    c.append(list(map(int, input().split())))
n1, m1 = map(int,input().split())
d = []
for i in range(n1):
    d.append(list(map(int, input().split())))
maxx = 0
ans = 0
maxy = 0
for i in range(n):
    for j in range(m):
        overlap = 0
        for k in range(n):
            for l in range(m):
                if i+k>n1 and j+l>m1:
                    overlap+=c[k][l]*d[k+i][j+l]
        print(overlap)
        if overlap>=ans:
            ans = overlap
            maxx = i
            maxy = j
print(maxx, maxy)
