from collections import deque

def charDif1(a,b):
    num=0
    for i in range(len(a)):
        if(a[i]!=b[i]):
            num+=1
    if(num==1):
        return True
    else:
        return False

def dfs(visited, begin, words, now, target):
    if(target == begin):
        return now
    for i in range(len(words)):
        if(visited[i]):
            continue
        if(charDif1(begin, words[i])):
            visited[i]=True
            num = dfs(visited, words[i], words, now+1, target)
            if(answer>num):
                answer=num
    return 999

def solution(begin, target, words):
    if target not in words:
        return 0
    visited=[False]*len(words)
    answer = dfs(visited, begin, words, 0, target)
    
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

        # queue = deque([(begin,0)])
        # while(queue):
        #     begin, now = queue.popleft()
        #     if(begin==target):
        #         if(now<answer):
        #             answer=now
        #     if charDif1(begin,w):
        #         queue.append((w,now+1))