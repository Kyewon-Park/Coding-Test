#배수와 약수

import sys
input = sys.stdin.readline

while(True):
    a,b = map(int, input().strip().split())
    if a == 0:
        break
    if a<b and b%a==0:
        print('factor')
    elif a>b and a%b==0:
        print('multiple')
    else:
        print('neither')