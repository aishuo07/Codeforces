n = int(input())
k = 1
b = []
for i in range(2, n):
    if n%i ==0 and i%k == 0:
        b.append(i)
        k = i
b = b[::-1]
if n == 1:
    print(1)
else:
    print(n, *b, 1)
