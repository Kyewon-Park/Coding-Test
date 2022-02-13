# 다리 놓기
from math import comb
import sys

input = sys.stdin.readline
n = int(input().strip())
for _ in range(n):
    a, b= map(int, input().strip().split())
    print(comb(b,a))