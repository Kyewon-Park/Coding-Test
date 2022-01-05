n=int(input())
d=[0]*(n+2)
d[1]=1
d[2]=3
if(n<3):
    print(d[n])
else:
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]*2
    print(d[n]%10007)