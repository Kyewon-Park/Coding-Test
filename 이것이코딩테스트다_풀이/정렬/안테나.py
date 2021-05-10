def ant():
    n = int(input())
    house = list(map(int,input().split()))
    s = sum(house)/4
    print(s)
    house.sort(key=lambda x:abs(x-s)) 
    print(house)
    print(house[0])
ant()