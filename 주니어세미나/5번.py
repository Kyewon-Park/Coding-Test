n,m=map(int,input().split())
nums = list(map(int,input().split()))
count=0
for i in nums:
    if i == m:
        count+=1
print(count)