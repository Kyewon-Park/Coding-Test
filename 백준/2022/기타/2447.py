def draw(n):
    if n==1:
        return ['*']
    stars = draw(n//3)    
    arr = []
    for star in stars:
        arr.append(star*3)
    for star in stars:
        arr.append(star+' '*(n//3)+star)
    for star in stars:
        arr.append(star*3)
    return arr
print(*draw(int(input())), sep='\n')