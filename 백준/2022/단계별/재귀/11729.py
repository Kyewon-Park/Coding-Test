#하노이

def hanoi(n, start, end, aux): #원판 n개를 start에서 end로 옮기기
    if n==1:
        print(start, end)      # 맨 밑 원판 1->3 로 옮김
    else:
        hanoi(n-1, start, aux, end) # n-1개를 보조기둥으로 옮기기
        print(start, end)
        hanoi(n-1, aux ,end, start)   # n-1개를 다시 보조기둥에서 끝으로 옮기기
        
n=int(input())
print(2**n-1)
print(hanoi(n, 1, 3, 2))