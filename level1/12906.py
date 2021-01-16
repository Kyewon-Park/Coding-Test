# level 1
# 같은 숫자는 싫어

arr = [1,1,3,3,0,1,0,1,1]	
answer = []

def solution(arr):    
    for idx, i in enumerate(arr[:-1]):
        if i == arr[idx+1]: 
            continue
        else: 
            answer.append(i)
    answer.append(arr[-1])
    return answer

print(solution(arr))