import sys
input = sys.stdin.readline
#랜선 자르기
k, n = map(int,input().split())
lines = [int(input()) for _ in range(k)]
result=0
start, end = 1, max(lines)
while(start<=end):
    mid=(start+end)//2
    all=0
    for i in lines:
        all += i//mid
    if all < n: #자른 개수가 목표 개수보다 부족하면 선 길이를 줄임.
        end = mid-1
    else: #최대한 덜잘랐을때
        start = mid+1
        result= mid
print(result)