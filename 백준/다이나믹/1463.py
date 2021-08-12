n=int(input())
d=[n+1]*(n+1)
d[1]=0
for i in [2,3]:
    for j in range(2,n+1):
        if j%i==0:
            d[j]=min(d[j//i]+1,d[j])
        else:
            d[j]=min(d[j-1]+1,d[j])
print(d[n])
