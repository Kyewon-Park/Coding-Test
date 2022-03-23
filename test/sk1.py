def solution(goods):
    l = len(goods)
    tl = [[] for i in range(l)]
    inLastLevel=False
    for k in range(l): #단어마다
        wordlen = len(goods[k])
        inLastLevel=False
        for i in range(1, wordlen+1): #i길이마다 
            if inLastLevel:
                break
            inLastLevel=False
            for j in range(wordlen-i+1): #j번만큼
                toAdd = goods[k][j:j+i]
                ISIN = True
                for x in range(l):
                    if x == k:
                        continue
                    if toAdd in goods[x]:
                        ISIN = False
                if ISIN:
                    if toAdd in tl[k]:
                        continue
                    tl[k].append(toAdd)
                    inLastLevel=True

    result=[]
    for l in tl:
        ans = ' '.join(sorted(l))
        result.append(ans)
    return result

print(solution(["abcdeabcd","cdabe","abce","bcdeab"]))