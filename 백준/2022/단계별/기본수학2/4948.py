#베르트랑 공준
arr = [True for _ in range(246913)]
arr[1]=False
for i in range(2,int(246912**0.5)+1):
    if arr[i]:
        j=2
        while i*j <= 246912:
            arr[i*j] = False
            j+=1
while(1):
    n = int(input())
    if n==0:
        break
    else:
        c=0
        for i in range(n+1,2*n+1):
            if arr[i]:
                c+=1
        print(c)