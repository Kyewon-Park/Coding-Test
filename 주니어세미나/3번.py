n=int(input())
num = list(map(int,input().split()))
nums=[]
for i in range(0,2*n,2):
    nums.append(num[i:i+2])
nums.sort()
print(nums)
top=0
for l in nums:
    if top<l[0]:
        break
    top=l[1]+l[0]
print(top)
    