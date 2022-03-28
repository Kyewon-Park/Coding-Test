#단지번호붙이기
import sys
input = sys.stdin.readline
map=[]
for i in range(7):
    map.append(list(map(int,input().strip().split())))

visited=[[False]*7 for _ in range(7)]