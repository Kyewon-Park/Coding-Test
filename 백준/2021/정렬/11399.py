n=int(input())
time = list(map(int,input().split()))
time.sort()
ans=0
for i in range(n):
    ans+=(n-i)*time[i]
print(ans)
# 1 2 3 3 4
# 1 1+2 1+2+3 1+2+3+3 1+2+3+3+4  