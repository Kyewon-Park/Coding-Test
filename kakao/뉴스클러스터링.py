# strex.isalpha()
# 교집합 set(str1) & set(str2)
# 합집합 set(str1) | set(str2) 

from string import ascii_letters
def solution(str1, str2):
    l1=[]
    l2=[]
    str1 = str1.upper()
    str2 = str2.upper()
    l1len = len(str1)-1
    l2len = len(str2)-1
    for i in range(l1len):
        if str1[i] in ascii_letters or str1[i+1] in ascii_letters:
            continue
        l1.append(str1[i:i+2])
    for i in range(l2len):
        if str2[i] in ascii_letters or str2[i] in ascii_letters:
            continue
        l2.append(str2[i:i+2])
    count=0
    for x in l1:
        if x in l2:
            l2.remove(x)
            count+=1
    l1len = len(l1)
    l2len = len(l2)
    ans = 65536 * (count/(l1len+l2len))
    return ans.floor()
