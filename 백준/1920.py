# 이진탐색
# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# m = int(input())
# b = list(map(int, input().split()))

# def check(num):
#     start = 0
#     end = n-1
#     while start<=end:
#         mid = (start+end)//2
#         if(num>a[mid]):
#             start = mid+1
#         elif(num<a[mid]):
#             end = mid-1
#         else:
#             return 1
#     return 0

# for i in b:
#     print(check(i))
import sys
input = sys.stdin.readline

n,A,m = input(),set(input().split()),input()
ans = ""
for i in input().split():
    ans+="1\n" if i in A else "0\n"
print(ans)


