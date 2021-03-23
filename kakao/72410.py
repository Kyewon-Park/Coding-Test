#2021 KAKAO BLIND RECRUITMENT
#신규 아이디 추천

import string
def solution(new_id):
    need = set(string.ascii_lowercase+'-_.0123456789')
    #1
    new_id = new_id.lower()
    print(f'1: {new_id}')
    
    #2
    li = [i for i in new_id if i in need]
    print(f'2: {li}')
    #3
    check=False
    for idx,c in enumerate(li):
        if c == '.':
            if(check==True):
                print(li.pop(idx))
                li.insert(idx,'');
            check=True
        else:
            check=False
    print(f'3: {li}')
    #4
    li = [*''.join(li).strip('.')]
    print(f'4: {li}')
    #5
    if(len(li) == 0):
        li.append('a')        
    #6
    print(len(li))
    if(len(li) >= 16):
        li = li[0:15]
        if(li[-1] =='.'):
            del li[-1]
    print(f'6: {li}')
    #7
    if(len(li) <= 2):
        while(len(li)<3):
            li.append(li[-1])
    print(f'7: {li}')

    return ''.join(li)