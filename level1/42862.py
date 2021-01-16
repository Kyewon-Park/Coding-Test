# 탐욕법Greedy
# level 1
# 체육복

def solution(n, lost, reserve):
    answer = n - len(lost)
    s_res = set(reserve)
    s_lost= set(lost)
    #먼저 중복되는 번호를 뺀다.
    s_and = s_res & s_lost
    answer += len(s_and)
    s_res -= s_and
    s_lost -= s_and

    for i in lost:
        if i-1 in s_res:
            answer +=1
            s_res.remove(i-1)
            continue
        if i+1 in s_res:
            answer +=1
            s_res.remove(i+1)
    
    return answer

solution(3, [1,2], [2,3])