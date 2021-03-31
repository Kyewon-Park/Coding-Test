# num, want_len = map(int,input().split())
# dduks = list(map(int,input().split()))
num, want_len = [4,6]
dduks = [19, 15, 10, 17]
dduks.sort(reverse=True)
maxd = dduks[0]

def myFunc():
    cut = 0 #절단기
    tops = []
    left=0
    while(left<want_len):
        cut+=1
        for i in dduks[len(tops):]:
            if(i == dduks[0]):
                tops.append(i)
            else:
                break
        for i in range(len(tops)):
            tops[i]-=1
            dduks[i]-=1
            left+=1
    print(maxd-cut)
    
