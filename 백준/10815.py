import sys
input = sys.stdin.readline

n,A,m = input(),set(input().split()),input()
ans = ""
for i in input().split():
    ans+="1\n" if i in A else "0\n"
print(ans)