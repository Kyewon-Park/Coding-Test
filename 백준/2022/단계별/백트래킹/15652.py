# #n과 m(4)
# import itertools
# n,m = map(int,input().split())
# for i in itertools.product(range(1,n+1), repeat=m):
#     jump=False
#     if len(i)>1:
#         before = i[0]
#         for j in i[1:]:
#             if j<before:
#                 jump=True
#                 break
#             before = j
#     if jump:
#         continue
#     else:
#         print(*i, sep=' ')

from itertools import combinations_with_replacement

n,m = map(int,input().split())
for i in combinations_with_replacement(range(1,n+1), r=m): 
    print(*i)