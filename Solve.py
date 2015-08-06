__author__ = 'twi'


class Solve:

    num = '0123456789'

    def __init__(self, sudokuIn):
        if self.hasRightForm(sudokuIn):
            self.x = []
            self.y = []
            self.z = []
            self.solutions = []
            self.setUp()
            if self.isValidSudoku(sudokuIn):
                self.sudokuIn = sudokuIn
            else:
                raise ValueError("not a valid input")
        else:
            raise ValueError("not a valid input")

    def anotherSudoku(self, sudokuIn):
        if self.hasRightForm(sudokuIn):
            oldX = self.x
            self.x = []
            oldY = self.y
            self.y = []
            oldZ = self.z
            self.z = []
            oldSolutions = self.solutions
            self.solutions = []
            self.setUp()
            if self.isValidSudoku(sudokuIn):
                self.sudokuIn = sudokuIn
            else:
                self.x = oldX
                self.y = oldY
                self.z = oldZ
                self.solutions = oldSolutions
                raise ValueError("not a valid input")
        else:
            raise ValueError("not a valid input")

    def isValidSudoku(self, sudokuIn):
        if self.hasRightForm(sudokuIn):
            i = 0
            while i < 9:
                i += 1
                j = 0
                while j < 9:
                    if j < len(self.x[i]):
                        if self.x[i][j] not in self.num:
                            raise ValueError("a not allowed character is in the input: {0}".format(self.x[i][j]))
                        if j+1 < len(self.x[i]):
                            if self.x[i][j] in self.x[i][j+1:]:
                                raise ValueError("{0} appears more than once in the input".format(self.x[i][j]))
                    if j < len(self.y[i]):
                        if self.y[i][j] not in self.num:
                            raise ValueError("a not allowed character is in the input: {0}".format(self.y[i][j]))
                        if j+1 < len(self.y[i]):
                            if self.y[i][j] in self.y[i][j+1:]:
                                raise ValueError("{0} appears more than once in the input".format(self.y[i][j]))
                    if j < len(self.z[i]):
                        if self.z[i][j] not in self.num:
                            raise ValueError("a not allowed character is in the input: {0}".format(self.z[i][j]))
                        if j+1 < len(self.z[i]):
                            if self.z[i][j] in self.z[i][j+1:]:
                                raise ValueError("{0} appears more than once in the input".format(self.z[i][j]))
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
        j = 0
        while i < 9:
            while j < 9:
                self.x[i] = "{0}{1}".format(self.x[i], sudokuIn[i][j])
                self.y[i] = "{0}{1}".format(self.y[i], sudokuIn[j][i])
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
                self.z[a] += sudokuIn[i][j]
                j += 1
            i += 1
