sum, limit = map(int, input().split())
l = []
for i in range(limit, 0, -1):
    c = bin(i)[2:]
    c = c[::-1]
    index = c.index('1')
    if sum-(2**index)>=0:
        sum = sum-(2**index)
        l.append(i)
    if sum == 0:
        break
if sum== 0:
    print(len(l))
    print(*l)
else:
    print(-1)
    

 
