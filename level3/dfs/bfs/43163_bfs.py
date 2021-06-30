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

def solution(begin, target, words):
    queue = deque([(begin,0, None)])
    answer=0
    wl=len(words)
    while(queue):
        begin, now, toRemov = queue.popleft()
        if(begin==target):
            if(now<answer):
                answer=now
                break;
        for i in range(wl-1):
            words_c = words[:]
            try:
                words_c.remove(toRemov)
            except ValueError:
                pass  # do nothing! 
            if charDif1(begin,words_c[i]):
                queue.append((words_c[i], now+1, begin))

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
