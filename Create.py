import random

__author__ = 'twi'

class Create:

    def __init__(self,writeToFile,file,solver):
        self.sudoku = []
        self.writeToFile = writeToFile
        self.file = file
        self.solver = solver
        self.createOneRandomCompleteSudoku(solver)

    def sudokuExists(self,sudoku):
        for i in self.sudokus:
            if self.equals(i,sudoku):
                return True
        return False

    def equals(self,s1,s2):
        x = 0
        while x < 9:
            y = 0
            while y < 9:
                if s1[x][y] != s2[x][y]:
                    return False
                y += 1
            x += 1
        return True

    # SHIT
    # does not work like that...
    def createOneRandomCompleteSudoku(self,solver):
        sudoku = ["","","","","","","","",""]
        x = ["","","","","","","","",""]
        y = ["","","","","","","","",""]
        z = ["","","","","","","","",""]
        i = 0
        random.seed()
        while i < 9:
            j = 0
            while j < 9:
                if i < 3:
                    a = 0
                elif i < 6:
                    a = 1
                else:
                    a = 2
                if j < 3:
                    a += 0
                elif j < 6:
                    a += 3
                else:
                    a += 6
                fill = random.randrange(0,4)
                if fill == 0:
                    num = random.randrange(1,10)
                    while "{0}".format(num) in x[i] or "{0}".format(num) in y[j] or "{0}".format(num) in z[a]:
                        num = random.randrange(1,10)
                    x[i] = "{0}{1}".format(x[i],num)
                    y[j] = "{0}{1}".format(y[j],num)
                    z[a] = "{0}{1}".format(z[a],num)
                    sudoku[i] = "{0}{1}{2}".format(sudoku[i][0:j],num,sudoku[i][j+1:])
                else:
                    sudoku[i] = "{0}{1}{2}".format(sudoku[i][0:j]," ",sudoku[i][j+1:])
                j += 1
            i += 1
        print(sudoku)
        print(x)
        print(y)
        print(z)
        solver.anotherSudoku(sudoku)
        solver.solveCall()
        print(solver.solutions[0])
        print(sudoku)
        self.sudoku = sudoku

# ok - methoden machen die halt solve-methoden sind wie menschen das machen würden
# damit das ganze dann nach schwierigkeit sortieren...

# zeilen- und spalten-weise permutationen in 3-er blöcken ausprobieren!! von einem einfachen sudoku das schon besteht

