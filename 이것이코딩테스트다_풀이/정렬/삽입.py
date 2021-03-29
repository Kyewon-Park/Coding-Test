def insertionSort(arr):
    for i in range(1,len(arr)): #몇개를?
        for j in range(i, 0, -1): #이만큼 반복
            if(arr[j-1] > arr[j]): #작으면 왼쪽으로
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

arr = [1,6,4,8,9,0,6,4,3,2]
print(insertionSort(arr))