# 별찍기10
# !!!!!!!!!!!!
def draw_star(n):
    global Map
    if n==3:
        Map[0][:3] = Map[2][:3] = ['*']*3
        Map[1][:3] = ['*',' ','*']
        return
    
    a = n//3
    draw_star(n//3)
    for i in range(3):
        for j in range(3):
            if i==1 and j==1: #가운데 부분
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어
N = int(input())      
Map = [[' ' for _ in range(N)] for _ in range(N)]
draw_star(N)
for i in Map :
    print(''.join(i))
