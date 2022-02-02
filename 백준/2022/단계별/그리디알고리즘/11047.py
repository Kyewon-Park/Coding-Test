#동전 0
import sys
input=sys.stdin.readline
n,k = map(int,input().strip().split())
coins = [int(input().strip()) for _ in range(n)]
left=k
ans=0
for i in coins[::-1]:
    if i>left:
        continue
    ans+=left//i
    left=left%i
print(ans)