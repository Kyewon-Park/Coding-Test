def dfs(n, arr):    
    if n==0:
        return arr
    a = arr
    a.append(n)
    n-=1
    return dfs(n, a)
    
n = int(input())
a = ['#']
print(dfs(n, a))