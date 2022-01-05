# 해시
# level 1
# 완주하지 못한 선수

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for idx, j in enumerate(completion):
        if j != participant[idx]:
            return participant[idx]
    return participant[-1]


'''
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''
