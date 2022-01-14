#벌집

import math
n=int(input())
if n==1:
    print(1)
else:
    print(math.floor(math.sqrt((n-1.25)/3)+0.5)+1)