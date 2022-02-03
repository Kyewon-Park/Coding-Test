s = input()
l = s.split('-')
ans = l[0]
ans = sum(map(int, ans.split('+')))
if len(l)>1:
    for i in l[1:]:
        ans-=sum(map(int,i.split('+')))
print(ans)