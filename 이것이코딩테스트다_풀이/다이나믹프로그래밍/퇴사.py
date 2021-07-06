n = int(input())
t = [0]*(n+1)
p= [0]*(n+1)
for i in range(1,n+1):
    ti, pi = map(int, input().split())
    t[i] = ti
    p[i] = pi

#===========

dp = [0]*(n+1)
for j in range(n,0,-1):
    if(t[j]+j > n):
        dp[j] = 0
        continue
    dp[j] = p[j] + dp[t[j]+j]

print(dp)