n = int(input())
li = list(map(int,input().split()))
d = [0]*(n+1)
d[0]=0
d[1]=li[0]
for i in range(2,n+1):
    d[i] = max(d[i-2]+li[i-1], d[i-1])
print(d[n])
