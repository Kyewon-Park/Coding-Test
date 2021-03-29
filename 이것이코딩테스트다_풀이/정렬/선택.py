def selectionSort(array):
    for i in range(len(array)):
        #가장 작은것을 선택해서 바꿈
        min_idx=i
        for j in range(i+1,len(array)):
            if array[j] < array[min_idx]:
                min_idx=j
        array[min_idx],array[i] = array[i],array[min_idx]
        print(array)
    return array

arr = [1,6,4,8,9,0,6,4,3,2]

print(f"1: {arr}")
array = selectionSort(arr)
print(f"2: {arr}")