#level 1
#문자열 내 마음대로 정렬하기

def solution(strings, n):
    for idx, i in enumerate(strings):
        strings[idx] = i[n] + i[0:n] + i[n+1:]
    strings = sorted(strings)
    for idx, i in enumerate(strings):
        strings[idx] = i[1:n+1] + i[0] + i[n+1:] 
    return strings

#다른 풀이
def solution(strings, n):
    return sorted(strings, key=lambda x: x[n])