#통계학
import sys
input = sys.stdin.readline
n=int(input())
l = [0]*4001
lm = [0]*4001
for _ in range(n):
    inp =int(input())
    if inp<0: 
        lm[abs(inp)]+=1
    else:
        l[inp]+=1
mean = int((sum(l) - sum(lm))/n)
print(f"{mean}")
for i in range(1,10001):
    if l[i]!=0:
        for _ in range(l[i]):
            print(i)