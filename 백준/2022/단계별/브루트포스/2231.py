#분해합
INF = 9999999
def getSum(N):
    l = list(map(int,str(N)))
    return N+sum(l)

arr=[INF]*1000001
for i in range(1,1000001):
    s = getSum(i)
    if s>1000000:
        continue
    if arr[s] > i:
        arr[s] = i

n = int(input())
print(0) if arr[n] == INF else print(arr[n])
