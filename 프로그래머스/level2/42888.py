def solution(record):
    action = ["Enter","Leave","Change"]
    result = []
    uidLog = [] 
    user = dict()
    for r in record:
        if(r[:5]==action[1]):
            a, uid = r.split()
            uidLog.append(uid)
            result.append("님이 나갔습니다.")
        else:
            a, uid, nick = r.split()
            if(a == action[0]): #enter
                uidLog.append(uid)
                result.append("님이 들어왔습니다.")
                user[uid] = nick
            elif(a == action[2]): #change
                user[uid] = nick
        
    
    for i in range(len(result)):
        result[i] = user[uidLog[i]] + result[i]
    
    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))