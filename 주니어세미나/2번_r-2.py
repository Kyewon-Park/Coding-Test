n=int(input())
A=list(map(int,input().split()))
B=[]
maxA=max(A)
for i in range(n-1):
    a=A[i]
    minA=maxA
    for j in A[i+1:]:
        if j>a:
            minA=min(minA,j)
    B.append(A.index(minA))

print(B)

# 6
# 2 4 3 5 1 6