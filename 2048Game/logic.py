# logic.py to be imported in the 2048.py file

# importing random package for methods to generate random numbers.
import random

# function to initialize game / grid at the start
def start_game():
    # declaring an empty list then appending 4 list each with four elements as 0.
    mat =[]
    
    for i in range(4):
        mat.append([0] * 4)

    # printing controls for user
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    # calling the function to add a new 2 in grid after every step
    add_new_2(mat)
    return mat

# function to add a new 2 to grid at any random empty cell
def add_new_2(mat):
   # choosing a random index for row and column.
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    #if random cell chosen is not empty, choose another one 
    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    # place a 2 at that empty random cell.
    mat[r][c] = 2

# function to get the current state of game
def get_current_state(mat):

    # if any cell contains 2048, game has been won
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 2048):
                return 'WON'

    # if there is at least one empty cell, game is not yet over
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 0):
                return 'GAME NOT OVER'

    # or if no cell is empty now but if after any move 
    # any two cells gets merged and creates an empty cell, game is not yet over
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
                return 'GAME NOT OVER'

    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return 'GAME NOT OVER'

    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return 'GAME NOT OVER'

    # else, game has been lost
    return 'LOST'

# all the functions defined below are for left swap initially.

# function to compress the grid after every step before and after merging cells.
def compress(mat):
    # bool variable to determine any change happened or not
    changed = False

    # empty grid 
    new_mat = []

    # with all cells empty
    for i in range(4):
        new_mat.append([0] * 4)
        
    # shift entries of each cell to it's extreme left row by row
    # loop to traverse rows
    for i in range(4):
        pos = 0

        # loop to traverse each column in respective row
        for j in range(4):
            if(mat[i][j] != 0):
                # if cell is non empty then shift it's number to
                # previous empty cell in that row denoted by pos variable
                new_mat[i][pos] = mat[i][j]
                
                if(j != pos):
                    changed = True
                pos += 1

    # returning new compressed matrix and the flag variable.
    return new_mat, changed

# function to merge the cells in matrix after compressing
def merge(mat):
    changed = False
    
    for i in range(4):
        for j in range(3):

            # if current cell has same value as next cell in the row and they
            # are non empty then
            if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):

                # double current cell value and empty the next cell
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0

                # make bool variable True indicating the new grid after
                # merging is different.
                changed = True

    return mat, changed

# function to reverse the content of each row (reversing the sequence)
def reverse(mat):
    new_mat =[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    return new_mat

# function to get the transpose of matrix means interchanging  rows and column
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

# function to update the matrix after moving / swiping left
def move_left(grid):

    # first compress the grid
    new_grid, changed1 = compress(grid)

    # then merge the cells.
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2

    # again compress after merging.
    new_grid, temp = compress(new_grid)

    # return new matrix and bool changed telling whether 
    # the grid is same or different
    return new_grid, changed

# function to update the matrix if moving / swiping right
def move_right(grid):

    # to move right, just reverse the matrix 
    new_grid = reverse(grid)

    # then move left
    new_grid, changed = move_left(new_grid)

    # then again reverse matrix will give desired result
    new_grid = reverse(new_grid)
    return new_grid, changed

# function to update the matrix after moving / swiping up
def move_up(grid):

    # to move up just taketranspose of matrix
    new_grid = transpose(grid)

    # then move left (calling all included functions) then
    new_grid, changed = move_left(new_grid)

    # again take transpose will give desired results
    new_grid = transpose(new_grid)
    return new_grid, changed

# function to update the matrix if moving / swiping down
def move_down(grid):

    # to move down, take transpose
    new_grid = transpose(grid)

    # move right and then again
    new_grid, changed = move_right(new_grid)

    # take transpose will give desired results.
    new_grid = transpose(new_grid)
    return new_grid, changed
