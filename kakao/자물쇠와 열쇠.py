import copy

def solution(key, lock):
    m = len(key)
    n = len(lock)

    #padding
    paddedLock = []
    pad = [0] * (2*m-2+n)
    for i in range(n):
        lock[i] = [0]*(m-1) + lock[i] + [0]*(m-1)

    for _ in range(m-1):
        paddedLock.append(pad)
    for row in lock:
        paddedLock.append(row)
    for _ in range(m-1):
        paddedLock.append(pad)

    ###    
    keys = []
    keys.append(key)
    for _ in range(3):
        key = list(zip(*key[::-1]))
        keys.append(key)
    ###
    for i in range(m+n-1):
        for j in range(m+n-1):
            for kn in range(4):
                flag=True
                #attach
                pl = copy.deepcopy(paddedLock)
                k = keys[kn]
                for a in range(m):
                    for b in range(m):
                        pl[i+a][j+b] = pl[i+a][j+b] ^ k[a][b]
                for x in range(n):          
                    for y in range(n):          
                        if pl[m-1+x][m-1+y]==0:
                            flag=False
                            break
                    if flag==False:
                        break
                if flag:
                    return True
    return False