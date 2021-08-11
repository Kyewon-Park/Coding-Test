#피보나치5
n=int(input())
d=[0]*23
d[0]=0
d[1]=1
for i in range(0,n+1):
    d[i+2]=d[i+1]+d[i]
print(d[n])