#2020 카카오 인턴십 67267

from itertools import permutations
from collections import deque

def solution(expression):
    le = len(expression)
    expression=list(expression)
    operand=set()
    for i in expression:
        if i=='+':
            operand.add('+')
        if i=='*':
            operand.add('*')
        if i=='-':
            operand.add('-')
    ol = list(permutations(operand, 3))
    for os in ol:
        for o in os:
            

solution("100-200*300-500+20")