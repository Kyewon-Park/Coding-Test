#위장
def solution(clothes):
    closet = dict()
    for a,b in clothes:
        if b not in closet:
            closet[b]=list()
        closet[b].append(a)
    ans=1
    for i in closet.values()
        ans*=(len(i)+1)
    return ans-1