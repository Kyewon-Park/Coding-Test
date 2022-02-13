#링
import sys
import math
input = sys.stdin.readline
n = int(input().strip())
l = list(map(int, input().strip().split()))
for i in l[1:]:
    g = math.gcd(l[0],i)
    print(str(l[0]//g) + '/' + str(i//g))