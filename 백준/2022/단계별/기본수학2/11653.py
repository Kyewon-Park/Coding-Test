#소인수분해
x = int(input())
n=x
i=2
while(n>1):
    if i>x:
        break
    if n%i==0:
        n=n//i
        print(i)
    else:
        i+=1