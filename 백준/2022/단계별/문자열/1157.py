#단어공부
import collections
s= input().upper()
c = collections.Counter(s).most_common()
if len(c)>1 and c[1][1] == c[0][1]:
    print("?")
else:
    print(c[0][0])