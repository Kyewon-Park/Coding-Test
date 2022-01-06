#한수

def oneNum(N):
    count=0
    if(N>=100):
        for i in range(100, N+1):
            l = list(map(int,str(i)))
            if l[1]-l[0] == l[2]-l[1]:
                count+=1
        return 99 + count
    else:
        return N
    
print(oneNum(int(input())))