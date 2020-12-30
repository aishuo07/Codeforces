n, k = map(int, input().split())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    d[i] = a[i]
maxi = 999999999999999999999
imd = 0
for i in range(k):
    c = (i+k)%n
    powe = a[i]
    while(c>i):
        powe+=a[c]
        c = (c+k)%n
    if maxi>powe:
        maxi = powe
        inde = i
print(inde+1)
