def solution(s):
    return [i.lower() if idx%2==0 else i.upper() for idx,i in enumerate(s)]

    lista = []
    for i, idx in enumerate(s):
        if(idx%2==0):
            lista.append(i.lower())
        else:
            lista.append(i.upper())
    return ''.join(lista)
s="tryhelloworld"
solution(s)