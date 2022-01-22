#n과 m(3)
import itertools
n,m = map(int,input().split())
for i in itertools.product(range(1,n+1), repeat=m):
    print(*i, sep=' ')