n,m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)
result=0
while start<=end:
    mid=(start+end)//2
    sum=0
    for t in trees:
        sum+=left if t-mid>0            
    if sum<m: #목표값보다 적게 얻으면 더 밑에를 자름
        end = mid-1
    else:
        result=mid
        start=mid+1
print(result)