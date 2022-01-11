#그룹 단어 체커
n = int(input())
ans = 0
for i in range(n):
    s= input()
    prev=''
    ss = set()
    isPass = True
    for c in s:
        if c in ss:
            if c == prev:
                continue
            else:
                isPass = False
                break
        else:
            ss.add(c)
            prev = c
    if isPass:
        ans += 1
print(ans)
