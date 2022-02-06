# #LCS
import sys
l1 = list(sys.stdin.readline().strip())
l2 = list(sys.stdin.readline().strip())
n = len(l1)
m = len(l2)
if n<m:
    l1,l2 = l2,l1
    n,m=m,n    
d = [0]*m
for i in range(n):
    maxl=0
    for j in range(m):
        if maxl < d[j]:
            maxl = d[j]
        elif l1[i]==l2[j]: 
            d[j]=maxl+1
print(max(d))
