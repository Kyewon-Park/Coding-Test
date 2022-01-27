# 0 1 타일

n=int(input())
d=[0]*3
d[1] = 1
d[2] = 2
for i in range(3,n+1):
    d[(i)%3]=(d[(i-1)%3]+d[(i-2)%3])%15746
else:
    print(d[n%3])