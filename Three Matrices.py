n = int(input())
l = []
for i in range(n):
    c = list(map(int, input().split()))
    l.append(c)
a = []
b = []
for i in range(n):
    a.append([-99999]*n)
    b.append([-99999]*n)
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = l[i][j]
            b[i][j] = 0
        elif a[i][j]==-99999:
            a[i][j] = a[j][i]= (l[i][j]+l[j][i])/2
            b[i][j] = (l[i][j]-l[j][i])/2
            b[j][i] = -1*(l[i][j]-l[j][i])/2
for i in a:
    for j in i:
        print(j, end = " ")
    print()
for i in b:
    for j in i:
        print(j, end = " ")
    print()
