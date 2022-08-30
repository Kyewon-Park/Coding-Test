def comp(arr,n):
    if len(arr) == 1:
        return arr[0][0]
    l = []
    nn = n//2
    # 왼쪽 위
    tl = comp([a[:nn] for a in arr[:nn]], nn)
    # 오른쪽 위
    tr = comp([a[nn:] for a in arr[:nn]] ,nn)
    # 왼쪽 아래
    dl = comp([a[:nn] for a in arr[nn:]] ,nn)
    # 오른쪽 아래
    dr = comp([a[nn:] for a in arr[nn:]] ,nn)
    s = tl+tr+dl+dr
    if s == '0000':
        return '0'
    elif s == '1111':
        return '1'
    else:
        return '(' + s + ')'

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))
print(comp(arr, n))
