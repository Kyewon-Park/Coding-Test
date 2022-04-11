class Node:
    def __init__(self, data, up=None, down=None):
        self.data = data
        self.down = down
        self.up = up
    
def solution(n, k, cmd):
    stack = []
    #노드생성
    now = Node(0)
    start = now
    for i in range(1,n):
        newNode = Node(i)
        now.down = newNode
        newNode.up = now
        now = newNode
    now = start
    #시작위치로 이동
    for i in range(k):
        now = now.down
    #cmd실행
    for c in cmd:
        if c[0]=='D':
            x, num = c.split()
            for i in range(int(num)):
                while now.down!=-1:
                    if now.down!=None:
                        now = now.down
                        break
                    else:
                        break
        elif c[0]=='U':
            x, num = c.split()
            for i in range(int(num)):
                while now.up!=-1:
                    if now.up!=None:
                        now = now.up
                        break
                    else:
                        break
        elif c[0]=='C':
            stack.append((now.data, now))
            now.data = -1
        elif c[0]=='Z':
            numBefore, location = stack.pop()
            location.data = numBefore
    
    now = start
    result=''
    for _ in range(n):
        if now.data==-1:
            result+='X'
        else:
            result+='O'
        now=now.down
    return result

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))

    # def solution(n, k, cmd):
    # stack = []
    # nodes = [True]*n
    # now = k
    # #cmd실행
    # for c in cmd:
    #     if c[0]=='D':
    #         x, num = c.split()
    #         for _ in range(int(num)):
    #             while not nodes[now+1]:
    #                 now+=1 
    #             now+=1
    #     elif c[0]=='U':
    #         x, num = c.split()
    #         for i in range(int(num)):
    #             while not nodes[now-1]:
    #                 now-=1 
    #             now-=1
    #     elif c[0]=='C':
    #         stack.append(now)
    #         nodes[now] = False
    #         preLoc = now
    #         if now==n-1:
    #             while not nodes[now-1]:
    #                 now-=1
    #             now-=1
    #         else:
    #             ifPass = False
    #             while not nodes[now+1]:
    #                 now+=1
    #                 if now==n-1:
    #                     now=preLoc
    #                     while not nodes[now-1]:
    #                         now-=1
    #                     now-=1
    #                     ifPass=True
    #                     break
    #             if not ifPass:
    #                 now+=1
                
    #     elif c[0]=='Z':
    #         location = stack.pop()
    #         nodes[location] = True
    
    # result=''
    # for i in range(n):
    #     if nodes[i]:
    #         result+='O'
    #     else:
    #         result+='X'
    # return result