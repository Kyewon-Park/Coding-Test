def solution(n, clockwise):
    answer = [[0]*n for _ in range(n)]
    start, d = [], []
    if clockwise:
        start = [(0, 0), (0, n-1), (n-1, n-1), (n-1, 0)]
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
    else:
        start = [(0, n-1), (0, 0), (n-1, 0), (n-1, n-1)]
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
    for i in range(4):
        turns=1
        count=0
        num = 0
        x, y = start[i][0], start[i][1]
        dX, dY = dx[i], dy[i]
        while num < (n*n) / 4:
            num += 1
            count += 1
            answer[x][y] = num
            if (n - turns) == count:
                dX = dx[(i+turns)%4]
                dY = dy[(i+turns)%4]
                count = turns
                turns += 1
            x += dX
            y += dY
    return answer
print(solution(5,False))