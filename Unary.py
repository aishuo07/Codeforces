dic = {">": 1000,
"<":1001,
"+":1010,
"-" :1011,
".":1100,
",":1101,
"[":1110,
"]": 1111}
st = ""
s = input()
for i in s:
    st+=str(dic[i])
sum = 0
for i in range(len(st)):
    if int(st[i]) == 1:
        sum+=2**(len(st)-(i+1))
print(sum%1000003)
        
