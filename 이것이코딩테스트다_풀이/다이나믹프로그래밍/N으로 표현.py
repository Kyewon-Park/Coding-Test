def solution(N, number):
    #초기화
    INF=int(1e9)
    dp=[INF]*32001
    dp[1]=2
    fixed=[1,11,111,1111,11111]
    for i in range(len(fixed)):
        if(fixed[i]*N>32000):
            continue
        dp[fixed[i]*N] = i+1
        print(f"dp[{fixed[i]}*{N}] = {dp[fixed[i]*N]}")
        print(f"dp[{fixed[i]}] = {dp[fixed[i]]}")

    for i in range(2,number+1):
        if(i*N>32000):
            mul=INF
        else:
            mul=dp[i*N]
        if(i%N==0):
            div=dp[i//N]
        else:
            div=INF
        dp[i]=min(dp[i-1]+1, dp[i], mul+1, dp[i+N]+1, dp[i-N]+1, div+1)
    
    print(f"dp[{number}]={dp[number]}")
    
    if dp[number]>8:
        return -1
    return dp[number]

solution(7,124)