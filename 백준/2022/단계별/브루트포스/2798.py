#블랙잭
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
l = sorted(list(map(int,input().split())))
maxi = l[0]+l[1]+l[2]
for i in range(n-2):
    ans = l[i]
    for j in range(i+1,n):
        ans += l[j]
        for k in range(j+1,n):
            ans += l[k]
            if ans <= m and ans > maxi:
                maxi = ans
            ans -= l[k]
        ans -= l[j]
    ans -= l[i]
print(maxi)