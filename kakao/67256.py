#2020 카카오 인턴십
#키패드 누르기

def solution(numbers, hand):
    result=[]
    neutral ='R'
    if hand=='left': neutral = 'L'
    arr = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    n_dict = {arr[i][j]: (i,j) for i in range(len(arr)) for j in range(len(arr[0]))}
    right = (3,2)
    left = (3,0)
    r_dist=0
    l_dist=0
    for n in numbers:
        if(n_dict[n][1] == 2):#오른쪽이면 
            result.append('R')
            right = n_dict[n]
        elif(n_dict[n][1] == 0):#왼쪽이면 
            result.append('L')
            left = n_dict[n]
        else:#중간이면
            r_dist = abs(n_dict[n][0]-right[0])+abs(n_dict[n][1]-right[1])
            l_dist = abs(n_dict[n][0]-left[0])+abs(n_dict[n][1]-left[1])
            if r_dist<l_dist:
                result.append('R') 
                right = n_dict[n]
            elif r_dist>l_dist:
                result.append('L') 
                left = n_dict[n]
            else: 
                result.append(neutral)
                if neutral == 'R':right = n_dict[n]
                else:left = n_dict[n]
    answer = ''.join(result)
    return answer