#셀프 넘버
def d(N):
    l=list(map(int,str(N)))
    return N+sum(l)

num = [True]*10000
for i in range(1,10000):
    n = d(i)
    if(n<10000):
        num[n]=False
for i in range(1,10000):
    if(num[i]):
        print(i)