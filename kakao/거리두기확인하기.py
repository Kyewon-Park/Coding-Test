def solution(places):
    ans = []
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for place in places:
        place = list(map(list, place))
        end=False
        for row in range(3):
            for col in range(5):
                if place[row][col] == 'P':
                    for d in range(4):
                        if row+dx[d]<0 or col+dy[d]<0 or row+dx[d]>4 or col+dy[d]>4:
                            continue
                        if place[row+dx[d]][col+dy[d]]=='D' or place[row+dx[d]][col+dy[d]]=='P':
                            ans.append(0)
                            end=True
                            break
                    if end:
                        break
                    for d in range(4):
                        if row+dx[d]<0 or col+dy[d]<0 or row+dx[d]>4 or col+dy[d]>4:
                            continue
                        if place[row+dx[d]][col+dy[d]]=='O':
                            place[row+dx[d]][col+dy[d]]='D'
            if end:
                break
        if not end:
            ans.append(1)
    return ans

print(solution([["POOOP", "OXXOX", "Odx", "OOXOX", "POXXP"], ["POOdx", "OXdxP", "dxXXO", "OXXXO", "OOOPP"], ["dxOdx", "OXOXP", "OXPOX", "OXXOP", "dxPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["dxP", "Xdx", "dxP", "Xdx", "dxP"]]))