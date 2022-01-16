#터렛

n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        d = ((x1-x2)**2 + (y1-y2)**2)**0.5
        if r1+r2 == d:
            print(1)
        else:
            if d == abs(r2-r1):
                print(1)
            elif d < abs(r2-r1):
                print(0)
            elif d > r1+r2:
                print(0)
            else:
                print(2)