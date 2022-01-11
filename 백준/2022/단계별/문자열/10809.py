#알파벳 찾기

import string
st = input()
l=list(string.ascii_lowercase)
for i in l:
    if i in st:
        print(st.index(i))
    else:
        print(-1)