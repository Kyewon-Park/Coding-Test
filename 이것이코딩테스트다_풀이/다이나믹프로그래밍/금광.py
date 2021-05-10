temp = "1 3 3 2 2 1 4 1 0 6 4 7"
a = list(map(int, temp.split()))
print(f"a = {a}")

n=3
m=4
dp=[]
for i in range(n):
    dp.append(a[m*i:m*(i+1)])
print(dp)

for i in range(n):
    for j in range(1,m):
        if(i==0):
            left_down=0
        else:
            left_down=dp[i-1][j-1]
        if(i==n-1):
            left_up=0
        else:
            left_up=dp[i+1][j-1]
        left = dp[i][j-1]
        dp[i][j] = max(left,left_down,left_up) + dp[i][j]
print(dp[n-1][m-1])