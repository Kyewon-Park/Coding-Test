def solution(n, k, cmd):
    stack = []
    nodes = [i for i in range(n)]
    now = k
    #cmd실행
    for c in cmd:
        if c[0]=='D':
            x, num = c.split()
            for _ in range(int(num)):
                while nodes[now+1]==-1:
                    now+=1 
                now+=1
        elif c[0]=='U':
            x, num = c.split()
            for i in range(int(num)):
                while nodes[now-1]==-1:
                    now-=1 
                now-=1
        elif c[0]=='C':
            stack.append(now)
            nodes[now] = -1
            preLoc = now
            if now==n-1:
                while nodes[now-1]==-1:
                    now-=1
                now-=1
            else:
                ifPass = False
                while nodes[now+1]==-1:
                    now+=1
                    if now==n-1:
                        now=preLoc
                        while nodes[now-1]==-1:
                            now-=1
                        now-=1
                        ifPass=True
                        break
                if not ifPass:
                    now+=1
                
        elif c[0]=='Z':
            location = stack.pop()
            nodes[location] = location
    
    result=''
    for i in range(n):
        if nodes[i] != i:
            result+='X'
        else:
            result+='O'
    return result
    
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))