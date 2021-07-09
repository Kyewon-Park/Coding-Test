import collections 

print(collections.Counter(input().lower()).most_common(1)[0][0].upper())