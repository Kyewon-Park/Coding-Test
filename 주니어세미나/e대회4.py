li = list(input().split(';'))
j = int(li[0])
s = int(li[1])
m = int(li[2])

ju = li[3:3+j]
su = li[3+j:3+j+s]
mo = li[3+j+s:-1]

answer= []

for i in ju:
    for j in su:
        for k in mo:
            answer.append(i+" "+j+" "+k)
answer=';'.join(answer)+';'
print(answer)