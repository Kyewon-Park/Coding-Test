#계수정렬로 풀이

n = 5
narray = [8,3,5,7,9]
m = 3
marray = [2,7,9]
# n = int(input())
# narray = list(map(int, input().split()))
# m = int(input())
# marray = list(map(int, input().split()))

def countSort():
    print("Using counting sort = ",end=" ")
    count = [0]*1000001
    for i in narray:
        count[i]+=1

    for i in range(1000001):
        for j in range(count[i]):
            print(i, end=" ")
    print()

# 집합자료형을 이용해 풀이
def setSort():
    print("Using set = ",end=" ")
    nset = set(narray)
    for i in marray:
        if i in nset:
            print("yes",end=" ")
        else:
            print("no",end=" ")

countSort()
setSort()