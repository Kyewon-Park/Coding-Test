#좌표 압축
import sys
n=int(sys.stdin.readline().strip())
l = list(map(int,sys.stdin.readline().strip().split()))
sl = sorted(list(set(l)))
dic = {v:i for i,v in enumerate(sl)}
ans=''
for i in l:
    ans += str(dic[i]) 
    ans += ' '
print(ans)