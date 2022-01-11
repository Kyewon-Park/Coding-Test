#다이얼

l = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
s = input()
ans = 0
for i in s:
    for a in range(len(l)):
        if i in l[a]:
            ans += 3+a
print(ans)