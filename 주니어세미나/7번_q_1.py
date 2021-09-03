# 어떤 배열 Array가 주어질 때, 가장 오랫동안 연속 상승한 길이와 가장 오랫동안 연속 하락한
# 길이를 순서대로 배열에 담아 return 하도록 output 함수를 완성하라.
# - 제한사항
# 배열의 길이는 5 이상 1000 이하.
# 배열의 원소는 1 이상 1000 이하.
# 만약 배열에 연속해서 증가하거나 감소한 길이가 모두 2 이하라면 정답 배열의 해당 위치에 1을 출력.

nums = list(map(int,input().split()))
#initialize
l=len(nums)
prev=nums[0]
upCount=1
downCount=1
maxUpCount=1
maxDownCount=1
def isMaxDown():
    global maxDownCount
    if maxDownCount<downCount:
        maxDownCount=downCount
def isMaxUp():
    global maxUpCount
    if maxUpCount<upCount:
        maxUpCount=upCount

for i in range(1,l-1):
    if nums[i]>prev: #새로운 수가 이전 수보다 크다면
        upCount+=1
        isMaxDown()
        downCount=1 #초기화
    elif nums[i]==prev: #같아서 upCount와 downCount둘다 초기화
        isMaxDown()
        downCount=1
        isMaxUp()
        upCount=1 
    else: #작으면 연속 상승한 길이를 max값과 비교하고 max값보다 크면 갱신.
        downCount+=1
        isMaxUp()
        upCount=1 #초기화
    prev=nums[i]

#마지막 상태가 아직 반영이 안됐으므로 
isMaxDown()
isMaxUp()
if maxDownCount<=2:
    maxDownCount=1
if maxUpCount<=2:
    maxUpCount=1
print(maxUpCount, maxDownCount)