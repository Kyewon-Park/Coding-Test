# 최대공약수 최소공배수

#유클리드 호제법
def gcf(x,y):
    while(True):
        r = x%y
        if r==0:
            break
        x = y
        y = r
    return y

def lcm(x,y,gcf):
    return (x*y)//gcf

a,b = map(int, input().split())
gc = gcf(a,b)
print(gc)
print(lcm(a,b,gc))
