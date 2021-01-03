n = sorted(list(input()))
k = sorted(list(input()))
a = {}
count = 0
flag = True
for i in k:
    if i in n:
        if i not in a:
            c= n.count(i)
            b = k.count(i)
            if c>=b:
                count+=b
            else:
                count+=c
            a[i] = 1
    else:
        flag = False
        break
if flag:
    print(count)
else:
    print(-1)
