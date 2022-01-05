#설탕배달
n=int(input())
arr=[3,5]
d=[5001]*(n+1)
d[0]=0
for i in range(2):
    for j in  range(arr[i],n+1):
        if d[j-arr[i]]!=5001:
            d[j] = min(d[j], d[j-arr[i]]+1)
if(d[n]!=5001):
    print(d[n])
else:
    print(-1)
        
