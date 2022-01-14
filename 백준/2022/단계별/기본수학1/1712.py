##손익분기점

a,b,c = map(int, input().split())
print(-1) if c-b < 1 else print(a//(c-b)+1)