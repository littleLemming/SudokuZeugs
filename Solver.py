import sys

class Solver:

    # solves regulat 9x9 sudokus
    # input as array-array, for empty spaces 0

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.valid(self.sudoku)
        self.solutions = []

    def finished(self,sudoku):
        for row in sudoku:
            row_tmp = list(filter((0).__ne__, sudoku[i]))
                if len(row_tmp) != len(set(row_tmp)):
                    return False
        return True

    def valid(self, sudoku):
        if len(sudoku) != 9:
            sys.exit("invalid sudoku: invalid size of sudoku")
        for i in range (0,9):
            # TODO: check if only 0-9 contained
            if len(sudoku[i]) != 9:
                sys.exit("invalid sudoku: invalid size of sudoku")
            row_tmp = list(filter((0).__ne__, sudoku[i]))
            if len(row_tmp) != len(set(row_tmp)):
                sys.exit("invalid sudoku: duplicates in row")
            column = [row[i] for row in sudoku]
            column_tmp = list(filter((0).__ne__, column))
            if len(column_tmp) != len(set(column_tmp)):
                sys.exit("invalid sudoku: duplicates in column")
        blocks = [[],[],[],[],[],[],[],[],[]]
        for i in range(0,3): # row
            for j in range(0,3): # column
                blocks[i*3+j].extend(sudoku[i*3][j*3:j*3+3])
                blocks[i*3+j].extend(sudoku[i*3+1][j*3:j*3+3])
                blocks[i*3+j].extend(sudoku[i*3+2][j*3:j*3+3])
        for i in blocks:
            block_tmp = list(filter((0).__ne__, i))
            if len(block_tmp) != len(set(block_tmp)):
                sys.exit("invalid sudoku: duplicates in block")

sudoku = [[1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],[4,5,6,7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
solver = Solver(sudoku)
