p,q,l,r = map(int,input().split())
a = []
b = []
count= 0
for i in range(p):
    n, m = map(int, input().split())
    a.append([n, m])
for i in range(q):
    n,m = map(int, input().split())
    b.append([n,m])
for k in range(l, r+1):
    flag = True
    for i in a:
        for j in b:
            if i[0]==j[0]+k or i[1] == j[1]+k or j[1]+k == i[0] or j[0]+k == i[1] or i[0]<=j[0]+k<=i[1] or i[0]<=j[1]+k<=i[1] or j[0]+k<=i[0]<=j[1]+k or j[0]+k<=i[0]<=j[1]+k:
                count+=1
                flag = False
                break
            
        if not flag:
            break
            
print(count)
