#직각삼각형

while(1):
    x=input() 
    if x=='0 0 0':
        break
    else:
        l = list(map(int,x.split()))
        if 0 in l:
            print('wrong')
            continue
        a,b,c = sorted(l)
        print('right') if c*c == b*b+a*a else print('wrong')