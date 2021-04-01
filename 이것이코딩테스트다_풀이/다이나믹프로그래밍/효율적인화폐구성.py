n,m = map(int, input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
d = [10001]*(max(m,max(coins))+1)

for i in coins:
    d[i] = 1

for i in range(2,m+1):
    if(d[i]!=10001):
        continue
    #배수면 1더함
    for j in range(n):
        if(i%coins[j]==0):
            d[i] = min(d[i], 1 + d[i-coins[j]])

if(d[m] == 10001):
    print(-1)
else:
    print(d[m])