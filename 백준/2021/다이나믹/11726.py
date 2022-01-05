#2*n타일링
n=int(input())
d= [0]*(n+2)
d[1]=1
d[2]=2
if n<=2:
    print(d[n])
else:
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
    print(d[n]%10007)

# n=int(input())
# s = [0, 1, 2]
# for i in range(3, 1001):
#   s.append(s[i - 2] + s[i - 1])
# print(s[n] % 10007)