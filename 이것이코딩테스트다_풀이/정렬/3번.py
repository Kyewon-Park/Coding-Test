n = int(input())
students = list(tuple(input().split()) for _ in range(n))
print(students)
print(*[s[0] for s in sorted(students, key = lambda x:int(x[1]))])
