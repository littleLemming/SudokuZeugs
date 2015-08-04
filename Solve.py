__author__ = 'twi'

class Solve:

    """
    form of a valid sudoku-input:

    it's an array. with nine strings in it. or arrays. it does not really matter.

    each of the strings can contain the numbers 0-9 or ' ' for not yet found numbers
    empty or other characters are not valid

    s1 = ["         ","         ","         ","         ","         ","         ","         ","         ","         "]
    s2 = [[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ']]
    are valid inputs for an empty sudoku.

    """

    num = '0123456789'

    def __init__(self,sudokuIn):
        if self.isValidSudoku(sudokuIn):
            self.sudokuIn = sudokuIn
            self.x = []
            self.y = []
            self.z = []
            self.setUp()
            print("gilt")
        else:
            raise ValueError("not a valid input")

    def anotherSudoku(self,sudokuIn):
        if self.isValidSudoku(sudokuIn):
            self.sudokuIn = sudokuIn
            self.x = []
            self.y = []
            self.z = []
            self.setUp()
            print("gilt")
        else:
            raise ValueError("not a valid input")

    # checks if the sudoku is valid - meaning:
    #   - are there the right characters?
    #   - is it the right size?
    #   - are there already combinations in a box/line that make the whole thing invalid?
    def isValidSudoku(self,sudokuIn):
        if self.hasRightForm(sudokuIn):
            i = 0
            z = ["","","","","","","","",""]
            while i < 9:
                x = []
                y = []
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
                    elif sudokuIn[i][j] != ' ':
                        raise ValueError("in a block there is one number multiple times")
                    j += 1
                i += 1
            return True
        raise ValueError("the form is not right. this error should not appear.")


    # checks if the sudoku is 9x9 (maybe later I will include other sizes? we'll see)
    def hasRightForm(self,sudokuIn):
        count = 0
        for i in sudokuIn:
            if len(i) == 9:
                count += 1
            else:
                raise ValueError("one of the lines is either too short or too long")
        if count != 9:
            raise ValueError("there are too many or too few lines in this sudoku")
        return True

    def setUp(self):
        return

    # stupidiest way of doing it =D
    # gives a list of all the possible solutions
    # x ... zeilen
    # y ... spalten
    # z ... kasterln
    def solve(self,sudoku,x,y,z,solutions):
        return