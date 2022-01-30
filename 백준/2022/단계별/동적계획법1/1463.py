n=int(input())
d=[0]*(n+1)
for j in range(2,n+1):
    d[j]=d[j-1]+1
    if j%3==0:
        d[j]=min(d[j//3]+1,d[j])        
    if j%2==0:
        d[j]=min(d[j//2]+1,d[j])
print(d[n])
