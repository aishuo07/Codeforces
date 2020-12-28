n  = int(input())
a = []
b = []
l = 0
for i in range(n):
    c = int(input())
    if c>0:
        a.append(c)
        if i == n-1:
            last = True
    else:
        b.append(-1*c)
        if i==n-1:
            last = False
if sum(a)>sum(b):
    print("first")
elif sum(a)<sum(b):
    print("second")
else:
    i = 0
    j = 0
    f = 0
    while(i<len(a) and j< len(b)):
        if a[i]>b[j]:
            print("first")
            f = 1
            break
        elif b[j]>a[i]:
            print("second")
            f = 1
            break
        i+=1
        j+=1
    if not f:
        if len(a)>len(b):
            print("first")
        elif len(a)<len(b):
            print("second")
        else:
            if last:
                print("first")
            else:
                print("second")
