import collections 

input = input().upper()
li = collections.Counter(input).most_common()
if len(li)>1 and li[0][1] == li[1][1]:
    print("?")
else:
    print(li[0][0])