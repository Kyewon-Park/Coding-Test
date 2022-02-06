#가장 긴 증가하는 부분수열 3

# 1 9 4 6 2 4 7 5 6 
# 1 9 
# 1 4
# 1 4 6 
# 1 2 6
# 1 2 4 
# 1 2 4 7
# 1 2 4 5
# 1 2 4 5 6 

import sys
from bisect import bisect_left
sys.stdin.readline()
l = list(map(int, sys.stdin.readline().strip().split()))
d = [[-9999999999]]
for i in l:
    for li in d:
        if li[-1] < i:
            li.append(i)
        else:
            d.append(li[:bisect_left(d, i)].append(i))
print(len(d)-1)


