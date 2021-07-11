x = [1,2,3,4]
y = list(range(1, 101))
z = [x%3 for x in y]
print(z.index(0))

print(x)
print(y)
print(z)