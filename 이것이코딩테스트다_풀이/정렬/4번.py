n,k = map(int, input().split())
alist = [*map(int,input().split())]
blist = [*map(int,input().split())]
print(alist, blist)

alist.sort()
blist.sort(reverse=True)
print(sum(blist[0:k])+sum(alist[k:]))