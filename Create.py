__author__ = 'twi'

class Create:

    def __init__(self,writeToFile,file,solver):
        self.sudokus = []
        self.writeToFile = writeToFile
        self.file = file
        self.solver = solver

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

    def createOneRandomCompleteSudoku(self,solver):
        sudoku = ["","","","","","","","",""]
        x = ["","","","","","","","",""]
        y = ["","","","","","","","",""]
        z = ["","","","","","","","",""]
        i = 0
        j = 0
        while i < 9:
            while j < 9:

                j += 1
            i += 1
        return sudoku