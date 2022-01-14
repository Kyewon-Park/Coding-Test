#acm 호텔 
for _ in range(int(input())):
    h,w,n = map(int, input().split())
    c = n//h+1
    a = n%h
    if a == 0:
        a=h
        c-=1
    print(str(a)+str(c).zfill(2))