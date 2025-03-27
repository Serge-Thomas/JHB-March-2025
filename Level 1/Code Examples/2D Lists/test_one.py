# 2D

# grayscale_image = [[236, 189, 189, 0],
#                    [236,  80, 189, 189],
#                    [236,   0, 189,  80],
#                    [236, 189, 189, 80]]

# List comprehension
# numbers_list = [2, 4, 6, 8]
# new_list = []
# for num in numbers_list:
#     new_list.append(num * 2)


# new_list = [num * 2 for num in numbers_list]
# print(new_list)

# USing list comprehension to create 2D list

# rows = 3
# cols = 4

# empty_grid = [[0] * cols for _ in range(rows)]
# # print(empty_grid)

# for row in empty_grid:
#     print(row)

# How to access or index an item in 2D list
# grid = [
#     [1, 2, 3],
#     ['A', 'B', 'C'],
#     ['#', "!", "*"]
# ]

# print(grid[1][1])

# grid[1] ==> ['A', 'B', 'C']
# grid[1][1] ==> 'B' 

# multiple items access
# grayscale_image = [[236, 189, 189, 0],
#                    [236,  80, 189, 189],
#                    [236,   0, 189,  80],
#                    [236, 189, 189, 80]]


# print(grayscale_image[2])

# for row in grayscale_image:     # loops through each row
#     # print(row)
#     for col in row:
#         print(col)


rows = 3
cols = 4

empty_grid = [[0] * cols for _ in range(rows)]
# print(empty_grid)

for row in empty_grid:
    print(row)