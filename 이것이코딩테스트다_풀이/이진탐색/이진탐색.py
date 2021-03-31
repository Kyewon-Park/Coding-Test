def binary_search1(array, target, start, end):#재귀
    if(start>end):
        return None
    mid = (start+end)//2
    if(target<array[mid]):
        res = binary_search1(array,target,start,mid-1)
    elif(target>array[mid]):
        res = binary_search1(array,target,mid+1,end)
    else:
        return mid
    return res

def binary_search2(array, target, start, end):#반복문
    mid = (start+end)//2
    while(start<=end):
        if(target<array[mid]):
            end = mid-1
        elif(target>array[mid]):
            start = mid+1
        elif(target==array[mid]):
            return mid
    return None
        

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search1(array, target, 0, n-1) #재귀
if(result == None):
    print("원소없음")
else:
    print(f"{result+1}번째 위치함")