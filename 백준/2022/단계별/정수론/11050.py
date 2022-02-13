#이항계수 1

from math import comb

n,k = map(int, input().split())
print(comb(n,k))