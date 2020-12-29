n, t = map(int, input().split())
a = list(map(int, input().split()))
i = 0
k = 0
maxi = 0
s = [0]*n
sum = 0
for j in range(n-1, -1,-1):
    sum+=a[j]
    s[j] = sum
while(i<n-maxi):
    sum = 0
    flag = False
    if t>=s[i]:
        if maxi<n-i:
            maxi = n-i
        break
    else:
        l = i+1
        r = n
        tar = s[i]-t
        while(l<r):
            mid = (l+r)//2
            if s[mid]>=tar:
                l = mid+1
            else:
                r = mid
        if maxi<l-(i+1):
            maxi = l-(i+1)
    i+=1
print(maxi)
