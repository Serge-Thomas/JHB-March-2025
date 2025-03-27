# Function to return new grid

def count_mines(grid):
    # rows = len(grid)
    # cols = len(grid[0])
    # new_grid = [[0] * cols for _ in range(rows)]
    
    size = len(grid)
    new_grid = [[0] * size for _ in range(size)]

    # print(new_grid)

    for row in range(size):
        for col in range(size):
            if grid[row][col] == '#':
                new_grid[row][col] = '#'
            else:
                count = 0
                
                # conditional for N E W S
                # check main directions
                #                   1-1=0   0
                if row > 0 and grid[row-1][col] == "#":    # north  
                    count += 1
                #                          1+1=2   0
                if row < size - 1 and grid[row+1][col] == "#":   # south 
                    count += 1
                
                if col > 0 and grid[row][col-1] == "#":   # west
                    count += 1 
                
                if col < size - 1 and grid[row][col+1] == "#":   # east
                    count += 1
                 
                 
                # Diagonally
                
                if row > 0 and col > 0 and grid[row-1][col-1] == "#":     # North west
                    count += 1
                if row > 0 and col < size - 1 and grid[row-1][col+1] == "#":   # North east 
                    count += 1
                
                if row < size - 1 and col > 0 and grid[row+1][col-1] == "#":   # South west
                    count += 1
                if row < size - 1 and col < size - 1 and grid[row+1][col+1] == "#":   # South east
                    count += 1

                new_grid[row][col] = count
                
                """
                  0    1    2    3    4
              0  ["-", "-", "-", "#", "#"],
              1  ["-", "#", "-", "-", "-"],
              2  ["-", "3", "#", "-", "-"],
              3  ["-", "#", "#", "-", "#"],
              4  ["-", "-", "-", "CP", "-"]
              
                [1, 2, 3, '#', '#']
                [2, '#', 4, 4, 2]
                [2, 4, '#', 3, 0]
                [2, '#', '#', 3, 0]
                [1, 2, 2, 1, 0]
                
                """
                
                
            

    return new_grid


grid_one = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
    ]

# print(grid_one)
grid = count_mines(grid_one)

for _ in grid_one:
    print(_)

for _ in grid:
    print(_)

"""
Expected Outcome
    [ [1, 1, 2, "#", "#"],
    [1, "#", 3, 3, 2],
    [2, 4, "#", 2, 0],
    [1, "#", "#", 2, 0],
    [1, 2, 2, 1, 0] ]

"""
