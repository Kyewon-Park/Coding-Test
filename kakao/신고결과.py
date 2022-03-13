def solution(id_list, report, k):
    l = len(id_list)
    report = list(set(report))
    count = [0]*l
    result= [0]*l
    arr = [[0]*l for i in range(l)]
    for r in report:
        reporter, reported = r.split(' ')
        x= id_list.index(reporter)
        y= id_list.index(reported)        
        arr[x][y]+=1
        count[y]+=1
    for i in range(l): # i = reported
        if count[i]>=k:
            for j in range(l): # j = reporter
                if arr[j][i]>0: 
                    result[j]+=1
    return result