# level 1
# 3진법 뒤집기

import math

def solution(n):
    answer = 0
    log = int(math.log(n,3))
    count = 0
    while n>0:
        answer+= n%3 * (3**(log - count))
        n=n//3
        count += 1  
        
    return answer