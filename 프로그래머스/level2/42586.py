import timeit

def solution(progresses, speeds):
    days = []
    for p,s in zip(progresses,speeds):
        quo = int((100-p)/s) #70/30 = 2
        if((100-p)%s!=0):
            quo+=1
        days.append(quo)

    for i in range(len(days)-1):
        if days[i+1] < days[i]:
            days[i+1] = days[i]
    
    return counts(days)

def counts():
    numbers = [5, 10,10,10, 15,15, 8,8,8,8]
    answer=[]
    now = numbers[0]
    count=1
    done=False
    for n in numbers[1:]:
        if now == n:
            count+=1
            done=False
        else:
            answer.append(count)
            count=1
            now=n
            done=True
    if(not done):
        answer.append(count)
    if(done):
        answer.append(1)
    return answer

print("'Manual' method average time:", timeit.timeit(counts, number=10000))