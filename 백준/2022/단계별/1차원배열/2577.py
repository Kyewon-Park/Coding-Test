#숫자의 개수
# from sys import stdin
# import collections
# input = stdin.readline
# n = int(input())*int(input())*int(input())
# l = collections.Counter(list(map(int,str(n))))
# for i in range(10):
#     print(l[i])

import time
#수정코드
start = time.time()

n = int(input())*int(input())*int(input())
s = str(n)
for i in range(10):
    print(s.count(str(i)))

print("time :", time.time() - start)

