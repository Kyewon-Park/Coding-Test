# level 1
# 두 개 뽑아서 더하기

def solution(numbers):
    val_set = set()
    for idx, i in enumerate(numbers):
        for j in numbers[idx+1:]:
            val_set.add(i+j)
    answer = list(val_set)
    answer.sort()
    return answer