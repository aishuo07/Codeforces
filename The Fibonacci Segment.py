n = int(input())
a = list(map(int, input().split()))
count = 2
maxi = 2
for i in range(2, n):
    if a[i] != a[i-1]+a[i-2]:
        if maxi<count:
            maxi = count
        count = 2
    else:
        count+=1
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(max(2, maxi,count))
