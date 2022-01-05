#최댓값
# from sys import stdin
# input = stdin.readline

# m=0
# c=0
# for i in range(9):
#     n = int(input())
#     if n > m:
#         m = n 
#         c = i+1
# print(m, c)

#수정 코드 
l = [int(input() for _ in range(9))]
print(max(l),l.index(max(l))+1)

