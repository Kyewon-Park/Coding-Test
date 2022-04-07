class Tree():
    def __init__(self):
        self.children = dict()
        self.count =0
    def insert(self,word):
        now = self
        for c in word:
            if c not in now.children:
                now.children[c]=Tree()
            now = now.children[c]
            now.count+=1
            
def solution(words, queries):
    result=[]
    root = [Tree() for _ in range(10001)]
    reverseRoot = [Tree() for _ in range(10001)]
    
    for word in words:
        wl = len(word)
        root[wl].insert(word)
        reverseRoot[wl].insert(word[::-1])
        
    for query in queries:
        ql = len(query)
        now = root[ql]
        
        if query[0] != '?':    
            for c in query:
                if c == '?':
                    result.append(now.count)
                    break
                else:
                    if c not in now.children:
                        result.append(0)
                        break       
                    now = now.children[c]
        else:
            if query[-1] == '?': #?????인 경우
                ans=0
                for i in now.children.values():
                    ans+=i.count           
                result.append(ans)
                break

            now = reverseRoot[ql]
            query = query[::-1]
            for c in query:
                if c == '?':
                    result.append(now.count)
                    break
                else:
                    if c not in now.children:
                        result.append(0)
                        break       
                    now = now.children[c]
    return result

    
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))