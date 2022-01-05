# 2019 카카오 겨울 인턴십
# level 1
# 크레인 인형뽑기 게임

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    bucket=[]
    height=len(board)

    for i in moves: # i-1번째 열
        for j in range(height):
            #먼저 빈 열인지 체크
            if board[height-1][i-1] == 0:
                break;
            #칸에 아무것도 없는가.
            if board[j][i-1] == 0: 
                continue
            #무언가가 있다면 bucket에 넣는다.
            bucket.append(board[j][i-1])
            board[j][i-1] = 0
            if len(bucket) >= 2:
                if(bucket[-1] == bucket[-2]):
                    bucket.pop(-1)
                    bucket.pop(-1)
                    answer+=2
            break;
    
    return answer

print(solution(board,moves))
