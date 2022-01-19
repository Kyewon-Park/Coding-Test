# 체스판 다시 칠하기
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

#기본 BW배열
baseArr = [[0]*8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            baseArr[i][j]='B'
        else:
            baseArr[i][j]='W'

#배열 비교 함수
def difNum(arr):
    count=0
    for i in range(8):
        for j in range(8):
            if baseArr[i][j] != arr[i][j]:
                count+=1
    return min(count,64-count)

#input입력
inputArr = []
for _ in range(n):
    inputArr.append(list(input().strip()))

ans=9999
for i in range(0,n-7):
    for j in range(0,m-7):
        arr = [inputArr[a][j:j+8] for a in range(i,i+8)]
        ans = min(ans, difNum(arr))

print(ans)