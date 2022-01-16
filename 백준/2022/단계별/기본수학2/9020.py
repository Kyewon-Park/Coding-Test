#골드바흐의 추측
arr=[True]*10001
for i in range(2, 101):
    if arr[i]:
        j=2
        while(i*j<=10000):
            arr[i*j]=False
            j+=1
n=int(input())
for _ in range(n):
    x=int(input())
    k=x//2
    while(k>=2):
        if arr[k]:
            if arr[x-k]:
                print(f'{k} {x-k}')
                break
        k-=1