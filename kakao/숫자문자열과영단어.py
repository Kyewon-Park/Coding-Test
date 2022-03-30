def solution(s):
    cha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(10):
        if cha[i] in s:
            s = s.replace(cha[i], num[i])
    return s

solution('one4seveneight')