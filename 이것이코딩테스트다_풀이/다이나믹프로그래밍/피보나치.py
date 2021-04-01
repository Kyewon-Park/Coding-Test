def fibo(n):
    made=[0]*(n+1)
    made[1]=1
    made[2]=2
    for i in range(3,n+1):
        made[i] = made[i-1]+made[i-2]
    return made[n]

print(fibo(99))
