def solution(integer):
    numList = list(map(int,list(str(integer))))
    l = len(numList)
    if(sum(numList[:l//2]) == sum(numList[l//2:])):
        return "LUCKY"
    else:
        return "READY"

print(solution(123402))