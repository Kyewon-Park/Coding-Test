# import string

# alp = list(string.ascii_lowercase)
# s = input()
# answer=''
# for i in alp:
#     if i in s:
#         idx = s.index(i)
#         answer+=str(idx)
#         answer+=" "

#     else:
#         answer+="-1 "

# print(answer)

mapped = map(chr, range(97,123))
print(list(map(input().find, mapped)))
