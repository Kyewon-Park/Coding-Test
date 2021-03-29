arr = [7,6,4,8,9,0,6,4,3,2,13]

def quick(arr,start,end):
    if(start>end):
        return
    pivot = start
    left = start + 1
    right = end 
    #right < left 일때 계속함
    while(right >= left):
        #왼쪽에서 pivot보다 큰걸 찾음 right
        while(right>start and arr[right]>=arr[pivot]):
            right-=1
        #오른쪽에서 pivot보다 작은걸 찾음 left
        while(left<=end and arr[left]<=arr[pivot]):
            left+=1
        #만약 right 위치가 lower위치보다 크면 pivot과 lower를 바꿈
        if(right<left):
            arr[pivot],arr[right] = arr[right],arr[pivot]
            break
        #두개 위치 바꿈
        else:
            arr[right],arr[left] = arr[left],arr[right]
    quick(arr,pivot,right-1)
    quick(arr,right+1,end)
#quick(arr,0,len(arr)-1)

def quick_as_python(arr):
    if(len(arr)<=1):
        return arr
    pivot = arr[0]
    tail = arr[1:]

    lefts = [x for x in tail if x <= pivot]
    rights = [x for x in tail if x > pivot]
    
    return quick_as_python(lefts)+ [pivot] + quick_as_python(rights)

print(quick_as_python(arr))
