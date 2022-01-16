#소수 구하기
arr = [True for _ in range(1000001)]
arr[1]=False
for i in range(2,1001):
    if arr[i]:
        j=2
        while i*j <= 1000000:
            arr[i*j] = False
            j+=1
a,b=map(int,input().split())

for i in range(a,b+1):
    if arr[i]:
        print(i)