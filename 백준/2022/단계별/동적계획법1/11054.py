#가장 긴 바이토닉 부분수열
m = int(input())
l = list(map(int,input().split()))
d=[1]*m
rd=[1]*m
for i in range(1,m):
    for j in range(i):
        if l[i] > l[j]:
            d[i] = max(d[i], d[j]+1)
        if l[m-i-1] > l[m-j-1]:
            rd[m-i-1] = max(rd[m-i-1], rd[m-j-1]+1)
for i in range(m):
    d[i] += rd[i]
print(max(d)-1)