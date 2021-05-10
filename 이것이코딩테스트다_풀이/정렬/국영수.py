def gys():
    n = int(input())
    score=[]
    for _ in range(n):
        score.append(input().split())
    score.sort(key = lambda s:(-int(s[1]),s[2],-int(s[3]),s[0]))
    for s in score:
        print(s[0])

gys()