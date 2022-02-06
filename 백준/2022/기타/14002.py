# 가장 긴 증가하는 부분수열 4
input()
l = list(map(int, input().split()))
n = len(l)
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j]+1)
m = max(dp)
print(m)
pl = ''
count = m
for i in range(n-1,-1,-1):
    if dp[i]==count:
        pl = str(l[i]) + ' ' + pl
        count-=1
print(pl)