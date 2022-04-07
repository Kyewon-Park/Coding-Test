from itertools import combinations
def solution(orders, course):
    result=[]
    for i in course:
        combPool = dict()
        for o in orders:
            cl = list(combinations(o,i))
            for c in cl:
                c = tuple(sorted(c))
                if c in combPool:
                    combPool[c]+=1
                else:
                    combPool[c]=1
        maxValue=0
        if list(combPool.values()) != []:        
            maxValue = max(combPool.values())
        if maxValue < 2:
            continue
        print(combPool)
        maxKeys = []
        for key in combPool:
            if combPool[key]==maxValue:
                maxKeys.append(key)
        for key in maxKeys:
            result.append(''.join(key))
    return sorted(result)

#----------------------
# import collections
# import itertools

# def solution(orders, course):
#     result = []

#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)

#         most_ordered = collections.Counter(order_combinations).most_common()
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

#     return [ ''.join(v) for v in sorted(result) ]