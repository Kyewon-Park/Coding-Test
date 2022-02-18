#연속합

n = int(input())
l = list(map(int,input().split()))
# cl = []
# plus = 0
# for i in l:
#     if i>=0:
#         plus += i   
#     else:
#         cl.append(plus)
#         cl.append(i)
#         plus=0
# ans=0
# anslist=[]
# while(n!=len(cl)-1):
#     minus=0
#     ans=0
#     for n,i in enumerate(cl):
#         if i<0:
#             minus=i
#         elif (minus+i)>=0:
#             ans+=(minus+i)
#             minus=0
#         else:
#             cl=cl[n:]
#             break;  
#     anslist.append(ans)
# print(max(anslist))