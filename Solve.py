__author__ = 'twi'

class Solve:

    """
    form of a valid sudoku-input:

    it's an array. with nine strings in it. or arrays. it does not really matter.

    each of the strings can contain the numbers 0-9 or ' ' for not yet found numbers

    """

    num = '0123456789'

    def __init__(self,sudokuIn):
        self.sudokuIn = sudokuIn

    # checks if the sudoku is valid - meaning:
    #   - are there the right characters?
    #   - is it the right size?
    #   - are there already combinations in a box/line that make the whole thing invalid?
    def isValidSudoku(self,sudokuIn):
        if self.hasRightForm(sudokuIn):
            # lines getting checked
            i = 0
            x = []
            y = []
            while i < 9:
                j = 0
                while j < 9:
                    if sudokuIn[i][j] in self.num and not sudokuIn[i][j] in x:
                        x = sudokuIn[i][j]
                    elif not sudokuIn[i][j] == ' ':
                        raise ValueError("there are not allowed characters in the input or too many of one")
                        return False
                    if sudokuIn[j][i] in self.num and not sudokuIn[j][i] in y:
                        y = sudokuIn[j][i]
                    elif not sudokuIn[j][i] == ' ':
                        raise ValueError("there are not allowed characters in the input or too many of one")
                        return False
                    j += 1
                i += 1
            # blocks getting checked

            # TODO

        raise ValueError("the form is not right. this error should not appear.")
        return False


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
