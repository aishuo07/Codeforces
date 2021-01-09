s = input()
prev = 0
lis = []
start = 0
flag = 0
for i in range(len(s)):
    if s[i] == '@' and prev == 0:
        if i-prev<=0:
            flag = 1
            break
        prev= i
    elif s[i] == '@':
        if i-prev>2:
            lis.append(s[start:prev+2])
            start = prev+2
            prev = i
            
        else:
            flag = 1
            break
if flag:
    print("No solution")
else:
    if s[start]!='@' and '@' in s[start:] and s[len(s)-1]!='@':
        lis.append(s[start:])
        for i in range(len(lis)-1):
            print(lis[i], end = ",")
        print(lis[len(lis)-1])
    else:
        print("No solution")
            
            
    
