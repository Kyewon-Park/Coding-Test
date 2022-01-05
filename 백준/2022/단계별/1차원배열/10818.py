#최소 최대

# input()
# a = list(map(int, input().split()))
# print(f"{min(a)} {max(a)}")


#수정 코드
import sys
input = sys.stdin.readline
input()
a = [int(_) for _ in input().split()]
print(min(a), max(a))