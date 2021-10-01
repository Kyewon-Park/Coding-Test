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
upCount=1   #연속 증가 수
downCount=1 #연속 감소 수
maxUpCount=1 #최대 연속 감소 수
maxDownCount=1 #최대 연속 감소 수

for i in range(1,l-1):
    if nums[i]>prev: #새로운 수가 이전 수보다 크다면
        upCount+=1
        maxDownCount=max(downCount,maxDownCount)
        downCount=1 #초기화
    elif nums[i]==prev: #같아서 upCount와 downCount둘다 초기화
        maxDownCount=max(downCount,maxDownCount)
        downCount=1
        maxUpCount=max(upCount,maxUpCount)
        upCount=1 
    else: #작으면 연속 상승한 길이를 max값과 비교하고 max값보다 크면 갱신.
        downCount+=1
        maxUpCount=max(upCount,maxUpCount)
        upCount=1 #초기화
    prev=nums[i]
# 마지막 상태가 아직 반영이 안됐으므로 
maxDownCount=max(downCount,maxDownCount)
maxUpCount=max(upCount,maxUpCount)

if maxDownCount<=2:
    maxDownCount=1
if maxUpCount<=2:
    maxUpCount=1
print(maxUpCount, maxDownCount)