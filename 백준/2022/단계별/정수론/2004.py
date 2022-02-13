#조합 0의 개수
a,b = map(int, input().split())
def countfive(n):
    cnt = 0
    while n != 0:
        n = n // 5
        cnt += n
    return cnt
def counttwo(n):
    cnt = 0
    while n != 0:
        n = n // 2
        cnt += n
    return cnt
f = countfive(a)-countfive(b)-countfive(a-b)
t = counttwo(a)-counttwo(b)-counttwo(a-b)
print(min(t,f))