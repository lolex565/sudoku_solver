f = open("sudoku.txt", "r")
f2 = open("sudoku_solved.txt", "a")

user_input = [[0 for y in range(9)]for x in range(9)]
program_output = [[0 for y in range(9)]for x in range(9)]
row_number = 0
column_number = 0

for line in f:
    for ch in line:
        if ch != "\n":
            user_input[row_number][column_number] = int(ch)
            column_number += 1
    row_number += 1
    column_number = 0

def possible(pos_x, pos_y, value):
    for y in range(9):
        if user_input[y][pos_x] == value:
            return False
    for x in range(9):
        if user_input[pos_y][x] == value:
            return False
    if pos_y < 3:
        if pos_x <3 :
            for k in range(3):
                for l in range(3):
                    if user_input[k][l] == value:
                        return False
        elif pos_x < 6:
            for k in range(3):
                for l in range(3,6):
                    if user_input[k][l] == value:
                        return False
        else:
            for k in range(3):
                for l in range(6,9):
                    if user_input[k][l] == value:
                        return False
    elif pos_y <6:
        if pos_x <3 :
            for k in range(3,6):
                for l in range(3):
                    if user_input[k][l] == value:
                        return False
        elif pos_x < 6:
            for k in range(3,6):
                for l in range(3,6):
                    if user_input[k][l] == value:
                        return False
        else:
            for k in range(3,6):
                for l in range(6,9):
                    if user_input[k][l] == value:
                        return False
    else:
        if pos_x <3 :
            for k in range(6,9):
                for l in range(3):
                    if user_input[k][l] == value:
                        return False
        elif pos_x < 6:
            for k in range(6,9):
                for l in range(3,6):
                    if user_input[k][l] == value:
                        return False
        else:
            for k in range(6,9):
                for l in range(6,9):
                    if user_input[k][l] == value:
                        return False
    return True
            
def solve():
    for y in range(9):
        for x in  range(9):
            if user_input[y][x] == 0:
                for n in range(1,10):
                    if possible(x,y,n):
                        user_input[y][x] = n
                        solve()
                        user_input[y][x] = 0
                return
        for x in  range(9):
            program_output[y][x] = user_input[y][x]   

solve()

temp_string = str()

for y in range(9):
    for x in range(9):
        temp_string += str(program_output[y][x])
    temp_string += "\n"
    f2.write(temp_string)
    temp_string = ""