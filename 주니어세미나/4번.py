n=int(input())
nset = set(map(int,input().split()))
m=int(input())
mlist = list(map(int,input().split()))
answer=""
for i in mlist:
    if i in nset: #set의 in 시간복잡도는 평균 O(1), 최악 O(n): Hash값 같을 시
        answer+="yes "
    else:
        answer+="no "
print(answer)