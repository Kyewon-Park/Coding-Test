# 완전탐색
# level 1
# 모의고사

def solution(answers):
    first=[1,2,3,4,5]
    second=[2,1,2,3,2,4,2,5]
    third=[3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    answer= []

    for idx, i in enumerate(answers):
        if i == first[idx%5]: 
            score[0] += 1
        if i == second[idx%8]: 
            score[1] += 1
        if i == third[idx%10]: 
            score[2] += 1
    
    max_val = max(score)
    for idx, i in enumerate(score):
        if i == max_val:
            answer.append(idx+1)
            
    return answer