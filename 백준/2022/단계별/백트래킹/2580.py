#스도쿠
import sys
from matplotlib.cbook import flatten
board = [list(map(int,sys.stdin.readline())) for _ in range(9)]

# for i in range(3):
#     for j in range(3):
#         sub = set(flatten(l[3*i:3*i+3][3*j:3*j+3]))
#         for i in range(9):
#             if len(sub) == 9 and 0 in sub:

for i in range(9):
    for j in range(9):
        if not board[i][j]: board.append([i,j])