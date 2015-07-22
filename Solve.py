import sys

__author__ = 'twi'


class Solve:
    """
    form of a valid sudoku-input:

    it's an array. with nine strings in it. or arrays. it does not really matter.

    each of the strings can contain the numbers 0-9 or ' ' for not yet found numbers

    """

    num = '123456789'

    def __init__(self, sudokuIn):
        """
        if self.isValidSudoku(sudokuIn):
            self.sudokuIn = sudokuIn
        else:
            raise ValueError("not a valid input")
        """

        self.solve_sudoku(sudokuIn)


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
                    if sudokuIn[i][j] in self.num and not sudokuIn[i][j] in x:
                        x = sudokuIn[i][j]
                    elif not sudokuIn[i][j] == ' ':
                        raise ValueError("there are not allowed characters in the input or too many of one")
                    if sudokuIn[j][i] in self.num and not sudokuIn[j][i] in y:
                        y = sudokuIn[j][i]
                    elif not sudokuIn[j][i] == ' ':
                        raise ValueError("there are not allowed characters in the input or too many of one")
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
                    if sudokuIn[i][j] != ' ' and not sudokuIn[i][j] in z[a]:
                        z[a] += sudokuIn[i][j]
                    else:
                        raise ValueError("in a block there is one number multiple times")
                    j += 1
                i += 1
            return True
        raise ValueError("the form is not right. this error should not appear.")

    # checks if the sudoku is 9x9 (maybe later I will include other sizes? we'll see)
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

    # stupidiest way of doing it =D
    # gives a list of all the possible solutions
    def solve(self):
        return

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
