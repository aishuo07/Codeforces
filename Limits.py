n,m  = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
if n == m:
    for i in range(2, min(abs(l[0]), abs(r[0]))+1):
        while l[0]%i == 0 and r[0]%i == 0:
            l[0]/=i
            r[0]/=i
    if r[0]>0:
        print(str(int(l[0]))+'/'+str(int(r[0])))
    elif r[0]<0 and l[0]>0:
        print('-'+str(int(l[0]))+'/'+str(int(r[0]))[1:])
    elif l[0]<0 and r[0]<0:
        print(str(int(l[0]))[1:]+'/'+str(int(r[0]))[1:])

elif n>m:
    if l[0]<0 and r[0]>0 or l[0]>0 and r[0]<0:
        print('-Infinity')
    else:
        print("Infinity")
else:
    print('0/1')
