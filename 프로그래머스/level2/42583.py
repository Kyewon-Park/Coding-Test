def solution(bridge_length, weight, truck_weights):
    lt = len(truck_weights)
    truck_pos = [0]*lt
    current_weight = 0
    current_length = 0
    for idx, i in enumerate(truck_weights):
        print(truck_pos)
        if(current_weight+i <= weight):
            if(current_length<= bridge_length):
                current_weight+=i
                current_length+=1
                truck_pos[:idx]+=1
        else:
            truck_pos[:idx-1]+=1
            idx-=1
    
    answer = 0
    return answer

solution(2,10,[7,4,5,6])