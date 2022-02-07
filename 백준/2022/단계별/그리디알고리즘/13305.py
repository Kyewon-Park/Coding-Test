#주유소

import sys
input = sys.stdin.readline
n = int(input().strip())
distance = list(map(int,input().strip().split()))
cost = list(map(int,input().strip().split()))[:-1]
minVal = cost[0]
sum = 0
for i in range(n-1):
    if minVal > cost[i]:
        minVal = cost[i]
    sum += (minVal * distance[i])
print(sum)
