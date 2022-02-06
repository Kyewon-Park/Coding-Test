# 가장 긴 증가하는 부분수열
# !!!!!!!!!!!!!
input()
l = list(map(int, input().split()))
n = len(l)
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
