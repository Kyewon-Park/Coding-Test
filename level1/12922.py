# level 1
# 수박수박수박수박수박

def solution(n):
    ans=[]
    for i in range(0,n,2):
        ans.insert(i, '수')
    for i in range(1,n,2):
        ans.insert(i, '박')
    answer = ''.join(ans)
    return answer