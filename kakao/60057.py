def solution(s):
    l = len(s)
    count = []
    for i in range(1,l//2+1):
        n = l
        for j in range(0,l-2*i+1, i):
            dup = False
            while(s[j:j+i]== s[j+i:j+2*i]):
                dup = True
                n -= i
                j+=i
            if(dup):
                n+=1
        count.append(n)
    print(count)
    return min(count)

solution("abcabcabcabcdededededede")