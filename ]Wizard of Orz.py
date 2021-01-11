s = "9890"
m = "1234567890"
for _ in range(int(input())):
    n = int(input())
    if n<=len(s):
        print(s[:n])
    else:
        res = s
        n-=len(s)
        for i in range(n//len(m)):
            res+=m
        res+=m[:n%len(m)]
        print(res)
