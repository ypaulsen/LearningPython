number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# To call items from inside 2D list: [row number][column number]. EG:
print(number_grid[0][2])
print(number_grid[2][2])

# Nested for loop to access elements in 2D list
for row in number_grid:
    for col in row:
        print(col)

