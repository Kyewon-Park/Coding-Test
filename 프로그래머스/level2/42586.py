#기능개발
import math
def solution(progresses, speeds):
    left = []
    for i in range(len(progresses)):
        left.append(math.ceil((100-progresses[i])/speeds[i]))
    print(left)
    result=[]
    past = left[0]
    count=1
    if len(left) > 1:
        for now in left[1:]: 
            if past<now:
                result.append(count)
                count=1
                past = now
            else:
                count+=1
    result.append(count)
        
    return result