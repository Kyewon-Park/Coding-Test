# 가장 긴 증가하는 부분수열
input()
l = list(map(int, input().split()))
order=0
endN=[0]
countN=[0]
for i in l:
    for j in range(order+1):
        if i > endN[j]:
            countN[j]+=1
            endN[j]=i
        else:
            order+=1
            endN.append(i)
            countN.append(0)
            break
print(max(countN))
