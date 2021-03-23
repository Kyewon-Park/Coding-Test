def solution(s):
    l = len(s)
    counts =[] 
    for i in range(1,l//2+1): #i개 단위일 때
        count=0
        for a in range(0,l,i):
            if (a+2*i >= l):
                break
            if (s[a:a+i]==s[a+i:a+2*i]):
                count+=1
        counts.append(count)
    print(counts)
    return max(counts)

solution("ababcdcdababcdcd")