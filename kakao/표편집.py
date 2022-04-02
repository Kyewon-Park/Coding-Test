def solution(n, k, cmd):
    li = [i for i in range(n)]
    stk = []
    idx = k
    for c in cmd:
        if c[0]=='D':
            a,b = c.split()
            b=int(b)
            idx+=b
            if idx>=n:
                idx=n-1
            
        elif c[0]=='U':
            a,b = c.split()
            b=int(b)
            idx-=b
            if idx<0:
                idx=0
            
        elif c[0]=='C':
            x = li.pop(idx)
            stk.append(x)
            
        else: # c[0]=='Z'
            x = stk.pop()
            li.append(x)
            li.sort()
    
    ans=''
    cnt=0
    for i in li:
        if i==cnt:
            ans+='O'
            cnt+=1
        else:
            while cnt < i:
                cnt+=1
                ans+='X'
            ans+='O'
            cnt+=1
    return ans
            
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))