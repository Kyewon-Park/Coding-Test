def pre(li, s):
    s += li[0]
    if di[li[0]][1] == '.' and di[li[0]][2] == '.':
        return s
    if li[1] != '.':
        s = pre(di[li[1]], s)
    if li[2] != '.':
        s = pre(di[li[2]], s)
    return s

#   0   1   2 
#   mid pre post
def post(li, s):    # (왼쪽 자식) (오른쪽 자식) (루트)
    if di[li[0]][1] == '.' and di[li[0]][2] == '.':
        s += li[0]
        return s
    if li[1] != '.':
        s = post(di[li[1]], s)
    if li[2] != '.':
        s = post(di[li[2]], s)
    s += li[0]
    return s

def mid(li, s):
    if di[li[0]][1] == '.' and di[li[0]][2] == '.':
        s += li[0]
        return s
    if li[1] != '.':
        s = mid(di[li[1]], s)
    s += li[0]
    if li[2] != '.':
        s = mid(di[li[2]], s)
    return s

di = dict()
n = int(input())
for i in range(n):
    a,b,c = list(input().split())
    di[a] = (a,b,c)

print(pre(di['A'], ''))
print(mid(di['A'], ''))
print(post(di['A'], ''))

