# 팩토리얼 0의 개수

def fact(n):
    ans = 1
    for i in range(2,n+1):
        ans*=i
    return ans
ans = 0
s = str(fact(int(input())))
for i in s[::-1]:
    if i == '0':
        ans+=1
    else:
        break
print(ans)