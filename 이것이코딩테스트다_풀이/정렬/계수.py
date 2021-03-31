import time

#counting sort
arr = [7,1,4,6,7,8,9,5,3,6,9,6,8,3,0,14,25,12,31,1,13,37,5,24,13,34,4,24,36,4,7]*1000
arr2 = [7,1,4,6,7,8,9,5,3,6,9,6,8,3,0,14,25,12,31,1,13,37,5,24,13,34,4,24,36,4,7]*1000


def countingSort1(arr):
    counts = [0]*(max(arr)+1) #배열길이+1
    #원소 개수 셈
    for a in arr:
        counts[a]+=1
    print("counts = " + str(counts))
    #정렬
    alist =[]
    for i in range(len(counts)):
        for _ in range(counts[i]):
            alist.append(i) 
    return alist



def countingSort2(arr):
    counts = [0]*(max(arr)+1) #배열길이+1
    #원소 개수 셈
    for a in arr:
        counts[a]+=1
    #print("counts 1= " + str(counts))
    
    #원소 앞에서부터 더함
    for i in range(len(counts)-1):
        counts[i+1] += counts[i] 
    #print("counts 2 = " + str(counts))

    for i in reversed(arr):
        arr[counts[i]-1] = i  #counts[i] = index
    return arr

print() 

start = time.time()
countingSort1(arr)
end = time.time()
print("arr1 time = " + str(end - start))

print() 

start = time.time()
countingSort2(arr2)
end = time.time()
print("arr2 time = " + str(end - start))



