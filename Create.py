__author__ = 'twi'

class Create:

    def __init__(self):
        self.sudoku = ["         ","         ","         ","         ","         ","         ","         ","         ","         "]
        self.sudokus = []


    # creates every possible sudoku. like. those are many. maybe they get written in a file or something.
    def createAll(self):

        return

    def sudokuExists(self,sudoku):
        for i in self.sudokus:
            if self.equals(i,sudoku):
                return True
        return False

    # s1 and s2 have to be completed sudokus - they do not have to be correct though
    # if they are completely the same, True, else False is
    def equals(self,s1,s2):
        x = 0
        y = 0
        while x < 9:
            while y < 9:

                y += 1
            x += 1