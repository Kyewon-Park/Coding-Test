n=int(input())
l = list(map(int,input().split()))
l.sort()
count=0 #그룹 수
i=0 #index
while i<n:
    #l[i]만큼 건너뛰기
    i+=l[i]
    if i>=n:
        break
    count+=1
print(count)