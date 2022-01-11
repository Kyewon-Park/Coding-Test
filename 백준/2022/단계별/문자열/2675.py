#문자열 반복

n=int(input())
for i in range(n):
    a,b =input().split()
    a=int(a)
    str=""
    for i in b:
        str+=a*i
    print(str)