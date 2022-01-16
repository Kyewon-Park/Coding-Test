#소수찾기
import math

n = int(input())
arr = [True for _ in range(1001)]
for i in range(2,int(math.sqrt(1000)+1)):
    if arr[i]==True:
        j=2
        while i*j <= 1000:
            arr[i*j] = False
            j+=1

l=list(map(int,input().split()))
c=0
for i in l:
    if i==1:
        continue
    if arr[i]:
        c+=1
print(c)