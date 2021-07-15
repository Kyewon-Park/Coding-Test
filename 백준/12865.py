n,k = map(int,input().split())
d=[100001]*(k+1)
d[0]=0
wv=[]
for _ in range(n):
    wv.append(tuple(map(int, input().split())))

for w,v in wv:
    for j in range(w,k+1):
        if(j%w==0 and j>w):
            continue
        if(d[j-w]!=100001 and d[j]!=100001):
            d[j]=max(d[j],d[j-w]+v)
        else:    
            d[j]=min(d[j],d[j-w]+v)

for i in range(k+1):
    if d[i]==100001:
        d[i]=0

print(d)
print(max(d))