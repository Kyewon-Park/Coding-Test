import math

def setSpendTime(time, inDict, car, timeDict):
    oh,om = map(int, time.split(':'))
    ih,im = map(int, inDict[car].split(':'))
    spendTime = (oh-ih)*60+(om-im)
    if car in timeDict:
        timeDict[car]+=spendTime
    else:
        timeDict[car]=spendTime

def solution(fees, records):
    basicTime, basicFee, perTime, perFee = map(int, fees)
    inDict=dict()
    timeDict=dict()
    fee=dict()
    #per record
    for r in records:
        time, car, inout = r.split(' ')
        if inout == 'IN':
            inDict[car] = time
        else:
            setSpendTime(time, inDict, car, timeDict)
            inDict.pop(car)
    #left
    for i in inDict.items():
        car, time = i
        oh,om = 23, 59
        ih,im = map(int, time.split(':'))
        spendTime = (oh-ih)*60+(om-im)
        if car in timeDict:
            timeDict[car]+=spendTime
        else:
            timeDict[car]=spendTime

    #calculate Fee
    for d in timeDict.items():
        car, spendTime = d
        totalFee = basicFee 
        left = (spendTime - basicTime)
        if left>0:
            totalFee += math.ceil(left/perTime)*perFee
        fee[car]=totalFee

    ans=[]
    keys = sorted(fee.keys())
    for k in keys:
        ans.append(fee[k])

    return ans
