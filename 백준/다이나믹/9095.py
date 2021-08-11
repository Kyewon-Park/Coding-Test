#123더하기
import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
d = [0]*11 #d[n]: n을 표현할 수 있는 경우의 수
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4,11):
    d[i] = d[i-1]+d[i-2]+d[i-3]
for i in nums:
    print(d[i]) 
