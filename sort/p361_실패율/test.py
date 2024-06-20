arr = [1,2,3]

print(sorted(enumerate(arr), key=lambda x: (-x[1], x[0])))