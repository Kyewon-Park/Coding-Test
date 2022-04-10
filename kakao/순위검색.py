class Tree:
    def __repr__(self):
        return "(%d, %d)" % (self.children, self.count)
    def __init__(self):
        self.children=dict()
        self.count=0
    def insert(self, il):
        now = self
        for i in il:  
            if i not in now.children:
                now.children[i] = Tree()
            now = now.children[i]
    def search(self, infoPart, i):
        now = self
        tempNow = self
        if infoPart[i].isdecimal():
            if int(list(now.children.keys())[0])<=int(infoPart[i]):
                now.count+=1
            return
        if infoPart[i] in now.children:
            now = now.children[infoPart[i]]
            now.search(infoPart, i+1)
        if '-' in list(tempNow.children.keys()):
            tempNow = tempNow.children['-']
            tempNow.search(infoPart, i+1)
        
def solution(info, query):
    root = Tree()
    now = root    
    for q in query:
        ql = list(q.replace('and ','').split())
        now.insert(ql)
    for i in info:
        now = root    
        infoPart = list(i.split())
        now.search(infoPart, 0)

    result=[]
    for q in query:
        ql = list(q.replace('and ','').split())
        now = root
        for i in ql:
            if i.isdecimal():
                result.append(now.count)
                continue
            elif i in now.children:
                now = now.children[i]
    return result

print(solution(	["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))

# class Tree:
#     def __init__(self):
#         self.children=dict()
#         self.count=0
#     def insert(self, info):
#         il = list(info.split())
#         now = self
#         for i in il:  
#             if i not in now.children:
#                 now.children[i] = Tree()
#             now.count+=1
#             now = now.children[i]
#     def search(self, ql):
#         tempResult = 0
#         for i in range(ql):
#             if ql[i].isdecimal():
#                 vl = now.children.values()
#                 for v in vl:
#                     if v>=ql[i]:
                        
#                 tempResult += now.count
                
#             if ql[i] == '-':
#                 for c in now.children:
#                     tempResult+= search(c,ql[i:])
#                 return tempResult
                
#             elif ql[i] in now.children:
#                 now = now.children[ql[i]]
                
#             else:
#                 return 0
        
# def solution(info, query):
#     root = Tree()
#     for i in info:
#         root.insert(i)
    
#     now = root    
#     for q in query:
#         ql = list(q.replace('and ','').split())
