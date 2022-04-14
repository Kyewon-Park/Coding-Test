#베스트 앨범

def solution(genres, plays):
    l = len(genres)
    total = dict()
    top = dict()
    for i in range(l):
        if genres[i] in total:
            total[genres[i]] += plays[i]
            top[genres[i]][i] = plays[i]
        else:
            total[genres[i]] = plays[i]
            top[genres[i]] = dict()
            top[genres[i]][i] = plays[i]

    sl = sorted(total.items(), key = lambda x:x[1], reverse=True)
    result=[]
    for genre, count in sl:        
        stl=sorted(top[genre].items(), key= lambda x:(-x[1], x[0]))[:2]
        for a,b in stl:
            result.append(a)
    return result

solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])