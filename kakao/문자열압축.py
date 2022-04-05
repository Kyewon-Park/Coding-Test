def solution(s):
    lens = len(s)
    n = lens//2
    counts=[]
    for l in range(1,n+1):
        count = lens
        prev = s[0:l]
        lastFixed=False
        overten=1
        for i in range(l,lens,l):
            if lens-i < l:
                break
            if s[i:i+l] == prev:
                count-=l
                overten+=1
                lastFixed=True
                if overten==10:
                    count+=1
            else:
                prev = s[i:i+l]
                overten=1
                if lastFixed:
                    count+=1
                    lastFixed=False
        if lastFixed:
            count+=1
        counts.append(count)
    if len(counts)!=0:
        return min(counts)
    else:
        return 1
        
print(solution('a'))