import sys

__author__ = 'twi'

class Solve:

    #########
    #   z   #
    #########
    # 0 3 6 #
    # 1 4 7 #
    # 2 5 8 #
    #########

    num = '123456789'

    def __init__(self, sudokuIn):
        if self.hasRightForm(sudokuIn):
            self.x = ["","","","","","","","",""]
            self.y = ["","","","","","","","",""]
            self.z = ["","","","","","","","",""]
            self.solutions = []
            self.setUp(sudokuIn)
            if self.isValidSudoku(sudokuIn):
                self.sudokuIn = sudokuIn
            else:
                raise ValueError("not a valid input")
        else:
            raise ValueError("not a valid input")

    def anotherSudoku(self, sudokuIn):
        if self.hasRightForm(sudokuIn):
            oldX = self.x
            self.x = ["","","","","","","","",""]
            oldY = self.y
            self.y = ["","","","","","","","",""]
            oldZ = self.z
            self.z = ["","","","","","","","",""]
            oldSolutions = self.solutions
            self.solutions = []
            self.setUp(sudokuIn)
            if self.isValidSudoku(sudokuIn):
                self.sudokuIn = sudokuIn
            else:
                self.x = oldX
                self.y = oldY
                self.z = oldZ
                self.solutions = oldSolutions
                raise ValueError("not a valid input")

    # checks if the sudoku is valid - meaning:
    #   - are there the right characters?
    #   - is it the right size?
    #   - are there already combinations in a box/line that make the whole thing invalid?
    def isValidSudoku(self, sudokuIn):
        if self.hasRightForm(sudokuIn):
            i = 0
            x = []
            y = []
            z = ["", "", "", "", "", "", "", "", ""]
            while i < 9:
                j = 0
                while j < 9:
                    if j < len(self.x[i]) and self.x[i][j] != ' ':
                        if self.x[i][j] not in self.num:
                            raise ValueError("a not allowed character is in the input: {0}".format(self.x[i][j]))
                        if j+1 < len(self.x[i]):
                            if self.x[i][j] in self.x[i][j+1:]:
                                raise ValueError("{0} appears more than once in the input".format(self.x[i][j]))
                    if j < len(self.y[i]) and self.y[i][j] != ' ':
                        if self.y[i][j] not in self.num:
                            raise ValueError("a not allowed character is in the input: {0}".format(self.y[i][j]))
                        if j+1 < len(self.y[i]):
                            if self.y[i][j] in self.y[i][j+1:]:
                                raise ValueError("{0} appears more than once in the input".format(self.y[i][j]))
                    if j < len(self.z[i]) and self.z[i][j] != ' ':
                        if self.z[i][j] not in self.num:
                            raise ValueError("a not allowed character is in the input: {0}".format(self.z[i][j]))
                        if j+1 < len(self.z[i]):
                            if self.z[i][j] in self.z[i][j+1:]:
                                raise ValueError("{0} appears more than once in the input".format(self.z[i][j]))
                    j += 1
                i += 1
            return True
        raise ValueError("the form is not right. this error should not appear.")

    def hasRightForm(self, sudokuIn):
        count = 0
        for i in sudokuIn:
            if len(i) == 9:
                count += 1
            else:
                raise ValueError("one of the lines is either too short or too long")
        if count != 9:
            raise ValueError("there are too many or too few lines in this sudoku")
        return True

    def setUp(self,sudokuIn):
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                if sudokuIn[i][j] != ' ':
                    self.x[i] = "{0}{1}".format(self.x[i], sudokuIn[i][j])
                if sudokuIn[j][i] != ' ':
                    self.y[i] = "{0}{1}".format(self.y[i], sudokuIn[j][i])
                if sudokuIn[i][j] != ' ':
                    a = 0
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
                    self.z[a] =  "{0}{1}".format(self.z[a], sudokuIn[i][j])
                j += 1
            i += 1

    def solveCall(self):
        self.solve(self.sudokuIn,self.x,self.y,self.z,0,0)

    def solve(self,sudoku,x,y,z,i,j):
        #print(sudoku)
        if i == 8 and j == 8 and sudoku[i][j] != ' ':
            print(sudoku)
            self.solutions.append(sudoku)
            return
        elif sudoku[i][j] == ' ':
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
            for n in range(1,10):
                nStr = "{0}".format(n)
                if nStr not in x[i] and nStr not in y[j] and nStr not in z[a]:
                    sudokuCp = sudoku[:]
                    xCp = x[:]
                    yCp = y[:]
                    zCp = z[:]
                    xCp[i] = "{0}{1}".format(xCp[i], n)
                    yCp[j] = "{0}{1}".format(yCp[j], n)
                    zCp[a] = "{0}{1}".format(zCp[a], n)
                    sudokuCp[i] = "{0}{1}{2}".format(sudokuCp[i][0:j],n,sudokuCp[i][j+1:])
                    ni = i
                    nj = j
                    if nj == 8:
                        nj = 0
                        ni += 1
                    else:
                        nj += 1
                    if i == 8 and j == 8:
                        print(sudokuCp)
                        self.solutions.append(sudokuCp)
                        return
                    self.solve(sudokuCp,xCp,yCp,zCp,ni,nj)
        else:
            sudokuCp = sudoku[:]
            xCp = x[:]
            yCp = y[:]
            zCp = z[:]
            ni = i
            nj = j
            if nj == 8:
                nj = 0
                ni += 1
            else:
                nj += 1
            self.solve(sudokuCp,xCp,yCp,zCp,ni,nj)

    ################################################################ works but not best performance ################################################################
    ################################################################ habs nett kommentiert :D       ################################################################

    #checks if the current number is in the same row as the number to be filled in
    def num_in_same_row(self,i,j):
        return (i/9 == j/9)

    #checks if the current number is in the same column as the number to be filled in
    def num_in_same_col(self,i,j):
        return (i-j) % 9 == 0

    #checks if the current number is in the same block as the number to be filled in
    def num_in_same_block(self,i,j):
        return (i/27 == j/27 and i%9/3 == j%9/3)

    """
    Solves the sudoku. It searches for an occuring 0 then it looks in the row,column and clock for already occuring numbers and adds them to
    a set of excluded numbers which may not be used at this place
    """
    def solve_sudoku(self,sudoku):
        i = sudoku.find('0')

        #checks if a 0 could be found if not then the sudoku should be completed.
        if i == -1:
            print("we are finished!")
            print(sudoku)
            sys.exit()

        excluded_numbers = set()

        #looks through all entries of the sudoku and find the exculded numbers in the row,column and block
        for j in range(81):
            if self.num_in_same_row(i, j) or self.num_in_same_col(i, j) or self.num_in_same_block(i, j):
                excluded_numbers.add(sudoku[j])

        #find the number which is not excluded at this point and puts it into place after that it runs the algorithm again to find all the other missing numbers
        for m in self.num:
            if m not in excluded_numbers:
                # print(sudoku[:i])
                self.solve_sudoku(sudoku[:i] + m + sudoku[i + 1:])

