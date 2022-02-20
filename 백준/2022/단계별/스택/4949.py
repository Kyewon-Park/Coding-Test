# 균형잡힌 세상

import sys
input = sys.stdin.readline
while(True):
    stk=[]
    flag=True
    l = list(input().rstrip('\n'))
    if len(l)==1 and l[0]=='.':
        break

    for i in l:
        if i=='(' or i=='[':
            stk.append(i)
        elif i==')':
            if len(stk)>0:
                if stk[-1]=='(':
                    stk.pop()
                else:
                    flag=False
                    break;
            else:
                flag=False
                break;
        elif i==']':
            if len(stk)>0:
                if stk[-1]=='[':
                    stk.pop()
                else:
                    flag=False
                    break;
            else:
                flag=False
                break;
    if(flag) and len(stk)==0:
        print('yes')
    else:
        print('no')
    