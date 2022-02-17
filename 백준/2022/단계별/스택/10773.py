#제로
import sys
input = sys.stdin.readline
N = int(input().strip())
l = []
for _ in range(N):
    n = int(input().strip())
    if n == 0:
        l.pop()
    else:
        l.append(n)
print(sum(l))