#소수

m=int(input())
n=int(input())

arr = [True]*10001
for i in range(2, 101):
    j=2
    while i*j<=10000:
        arr[i*j] = False
        j+=1
sum=0
minv=10000
arr[0]=False
arr[1]=False

for i in range(m,n+1):
    if arr[i]:
        sum+=i
        if minv > i:
            minv=i
if sum==0:
    print(-1)
else:
    print(sum)
    print(minv)
