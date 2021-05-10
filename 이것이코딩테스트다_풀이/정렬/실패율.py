def solution(N, stages):
    ilist = []
    totallist = []
    for i in range(1,N+1):
        icount= 0
        upcount = 0
        for s in stages:
            if i == s:
                icount+=1
            elif i < s:
                upcount+=1        
        ilist.append(icount)        
        totallist.append(icount+upcount)
    failure = []
    for a,b in zip(ilist,totallist):
        failure.append(a/b) if b!= 0 else failure.append(0)
    sortedfailure = sorted(range(1,len(failure)+1), key= lambda x: failure[x-1],reverse=True)
    return sortedfailure