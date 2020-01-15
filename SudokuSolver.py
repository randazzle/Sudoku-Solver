question = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]


#printing the board
def display(qw):

    for i in range(len(qw)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")
        
        for j in range(len(qw[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(str(qw[i][j]) + " | ")
            else:
                print(str(qw[i][j]) + " ", end="")

#finding empty box or having 0
def find_empty(qw):

    for i in range(len(qw)):
        for j in range(len(qw[i])):
            if qw[i][j] == 0:
                return (i, j)       #row, column

    return None

#checking if the input is valid according to Sudoku rules
def check(qw, num, pos):
    
    #Checking row
    for i in range(len(qw[0])):
        if qw[pos[0]][i] == num and pos[1] != i:
            return False

    #checking column
    for j in range(len(qw[0])):
        if qw[j][pos[1]] == num and pos[0] != j:
            return False

    #checking box

    #locating which 3x3 box
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_y * 3, box_y *3 +3):
        for j in range(box_x * 3, box_x *3 +3):
            if qw[i][j] == num and pos == (i, j):
                return False

    return True

#solving recursively
def solve(qw):

    box = find_empty(qw)

    if not box:
        return True
    else:
        row, col = box

    for i in range(1,10):
        if check(qw, i, (row,col)):
            qw[row][col] = i

            if solve(qw):
                return True

            qw[row][col] = 0
    
    return False

#MAIN FUNCTION
def main():
    
    display(question)
    solve(question)
    print("/////////////////////////////")
    display(question)


if __name__ == "__main__":
    main()
