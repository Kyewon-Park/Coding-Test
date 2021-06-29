#타켓 넘버

from collections import deque 
def solution(numbers, target):
    answer=0
    queue=deque([(0,0)])
    while(queue):
        current_sum, idx = queue.popleft()
        if(idx==len(numbers)):
            if(current_sum==target):
                answer+=1
        else:
            number = numbers[idx];
            queue.append((current_sum+number,idx+1))
            queue.append((current_sum-number,idx+1))
    return answer

solution([1, 1, 1, 1, 1],3)