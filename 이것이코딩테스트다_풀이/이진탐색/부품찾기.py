#이진탐색으로 

n = int(input())
narray = list(map(int, input().split()))
m = int(input())
marray = list(map(int, input().split()))

#n 정렬
narray.sort()

#marray 순차 이진탐색
def bisearch(narray,marray,start,end):
    answer = []
    for target in marray:
        appended = False
        start = 0
        end = len(narray)-1
        while(start<=end):
            mid = (start+end)//2
            if(target<narray[mid]):
                end = mid-1
            elif(target>narray[mid]):
                start = mid+1
            elif(target==narray[mid]):
                answer.append("yes")
                appended=True
                break;
        if(appended):
            continue
        answer.append("no")
    return answer

print(bisearch(narray,marray,0,len(narray)-1))