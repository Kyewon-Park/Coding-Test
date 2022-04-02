from itertools import combinations
def solution(relation): 
    answer = []
    combs=[]
    colnum = len(relation[0])
    for i in range(1,colnum+1):
        combs.append(list(combinations(range(colnum), i)))
    for i in range(colnum):
        for c in combs[i]: # c = (1,2)
            skipThisC = False
            keyPool=[]
            for row in relation:
                currentKey = [row[i] for i in c]
                if currentKey in keyPool:
                    skipThisC = True
                    break
                keyPool.append([row[i] for i in c])
            if not skipThisC:
                put=True
                for a in answer:
                    if set(a).issubset(c):
                        put=False
                        break
                if put:
                    answer.append(c)
    return len(answer)
    
solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])