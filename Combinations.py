n = int(input())
c = []
for i in range(n):
    a, b = map(int, input().split())
    c.append([b,a])
c = sorted(c, reverse = True)
count = 1
sum = 0
for i in c:
    if count==0:
        break
    count-=1
    sum+=i[1]
    count+=i[0]
print(sum)
