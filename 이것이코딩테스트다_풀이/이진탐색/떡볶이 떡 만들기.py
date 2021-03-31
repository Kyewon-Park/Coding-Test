# num, want_len = map(int,input().split())
# dduks = list(map(int,input().split()))
num, want_len = [4,6]
dduks = [19, 15, 10, 17]

def myFunc():
    dduks.sort(reverse=True)
    maxd = dduks[0]
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
    
def bisearch():
    end = max(dduks)
    start = 0
    result = 0
    while(start<=end):
        left = 0
        mid = (end+start)//2
        for i in dduks:
            if(i>mid):
                left+= i-mid
        if(left<want_len):#만약 덜짤렸다면
            end = mid-1
        else:
            start = mid+1
            result = mid
    return result

print(bisearch())
            
