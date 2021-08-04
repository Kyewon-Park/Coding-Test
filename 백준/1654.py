#랜선 자르기
n,k = map(int,input().split())
lines = [int(input()) for _ in range(n)]

def check():
    start=1
    end=min(lines)
    while(start<=end):
        prevStart=start
        mid=(start+end)//2
        all=0
        for i in lines:
            all += i//mid
        if all < k:
            end = mid+1
        else:
            start = mid-1
            if(prevStart==start):
                return mid
    return mid

print(check())
