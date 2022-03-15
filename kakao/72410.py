#2021 KAKAO BLIND RECRUITMENT
#신규 아이디 추천

import string
def solution(new_id):
    #1
    new_id = new_id.lower()
    print(new_id)
    #2
    need = set(string.ascii_lowercase+'-_.0123456789')
    li = [i for i in new_id if i in need]
    new_id=''.join(li)
    print(new_id)
    
    #3
    while(".." in new_id):
        new_id = new_id.replace("..",".")
    print(new_id)
    #4
    new_id = new_id.strip('.')
    print(new_id)
    #5
    if(len(new_id) == 0):
        new_id+='a'
    print(new_id)
    #6
    li = list(new_id)
    if(len(li) >= 16):
        li = li[0:15]
        if(li[-1] =='.'):
            del li[-1]
    print(li)
    #7
    if(len(li) <= 2):
        while(len(li)<3):
            li.append(li[-1])
    return ''.join(li)

solution('...!@BaT#*..y.abcdefghijklm')