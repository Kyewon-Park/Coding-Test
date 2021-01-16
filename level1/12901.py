# level 1
# 2016년

#1
def solution1(a, b):
    day = 'THU,FRI,SAT,SUN,MON,TUE,WED'.split(',')
    month =[31,29,31,30,31,30,31,31,30,31,30,31]
    return day[(sum(month[:a-1])+b)%7]


#2
def solution2(a, b):
    day ={1:'FRI',2:'SAT',3:'SUN',4:'MON',5:'TUE',6:'WED',0:'THU'}
    days =[31,29,31,30,31,30,31,31,30,31,30,31]
    num=0
    
    for i in range(a-1):
        num+=days[i]
    answer = day[(num+b)%7]
    return answer