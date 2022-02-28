# 요세푸스
n, k = map(int, input().split())
li = [i for i in range(n)]
ans=[]
for _ in range(n):
    while li[k]==False:
        k+=1
        if k>=n:
            k-=n
    ans.append(li[k])
    li[k]=False
    x=0
    while x!= 3:
        k+=1
        if k>=n:
            k-=n
        if li[k]==True:
            x+=1
           
    

print(f"<{','.join(ans)}")
