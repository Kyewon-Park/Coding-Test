from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)
    on = deque([])
    time = deque([])
    count = 0
    while(queue or time):
        #시간 지나면 다리에서 나감
        if(len(time)>0 and count-time[0]==bridge_length):
            on.popleft()
            time.popleft()
        #견딜만하면 추가
        if(len(queue)>0 and queue[0]+sum(on)<=weight): 
            popped = queue.popleft()
            on.append(popped)
            time.append(count)
        count+=1
    return count

solution(2,10,[7,4,5,6])