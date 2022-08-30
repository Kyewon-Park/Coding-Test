# import copy 
# def dfs(l,sarr):
#     if len(sarr) == 6:
#         print(*sarr)
#         return
#     for i in l:
#         if len(sarr) > 0 and sarr[-1] > i:
#             continue
#         tsarr = copy.deepcopy(sarr)
#         tl = copy.deepcopy(l)    
#         tsarr.append(i)
#         tl.remove(i)
#         dfs(tl,tsarr)
from itertools import combinations
      
input1 = ''
ans = []
while(input1 != '0'):
    input1 = input()  
    num = list(map(int, input1.split()))
    # dfs(num[1:], ans)
    combs = combinations(num[1:], 6)
    for c in combs:
        print(*c)
    print()