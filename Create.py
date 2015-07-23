__author__ = 'twi'

class Create:

    #    --> y
    #    _______
    #   |       |    |
    #   |       |    |
    #   |       |    V
    #    -------
    #                x
    #
    # just. yes. that's how it works. so i know. =D

    # writeToFile
    #   if True, the sudokus will be safed
    # file
    #   file in that will be written if writeToFile is true
    def __init__(self,writeToFile,file):
        self.sudokus = []
        self.writeToFile = writeToFile
        self.file = file


    # creates every possible sudoku. like. those are many. maybe they get written in a file or something.
    # notAllowed
    #   is an array-array that contains an empty string for each position in the sudoku
    #   if something is inserted the lines and blocks in contact will be updated so that it is not possible to
    #   put in a wrong number
    # sudoku
    #   the sudoku right now - as input: ["         ","         ","         ","         ","         ","         ","         ","         ","         "] please..
    # x
    #   int between 0 and 8, has to be 0 for the first call
    # y
    #   int between 0 and 8, has to be 0 for the first call
    # num
    # int between 1 and 9 - in the beginning 1
    def createAll(self,x,y,notAllowed,sudoku,num):
        if x < 0 or x > 8 or y < 0 or y > 8 or num < 1 or num > 9:
            return
        if x == 8 and y == 8:
            self.sudokus.append(sudoku)
        if num < 9:
            sudokuCopy = sudoku[:]
            notAllowedCopy = notAllowed[:]
            self.createAll(x,y,notAllowedCopy,sudokuCopy,num+1)
        sudokuCopy = sudoku[:]
        notAllowedCopy = notAllowed[:]

        # TRY DOING THINGS LIKE UPDATING NOT ALLOWED : START

        if y < 9:
            for i in range(y+1,9):
                notAllowedCopy[x][i] = "{0}{1}".format(notAllowed[x][i],num)

        if x < 9:
            for i in range(x+1,9):
                notAllowedCopy[i][y] = "{0}{1}".format(notAllowed[i][y],num)

        # TODO: BLOCKS ARE MISSING!!

        # TRY DOING THINGS LIKE UPDATING NOT ALLOWED : END

        sudokuCopy[x][y] = num
        if y < 8:
            self.createAll(x,y+1,notAllowedCopy,sudokuCopy,num)
        else:
            self.createAll(x+1,y,notAllowedCopy,sudokuCopy,num)
    def sudokuExists(self,sudoku):
        for i in self.sudokus:
            if self.equals(i,sudoku):
                return True
        return False

    # s1 and s2 have to be completed sudokus - they do not have to be correct though
    # if they are completely the same, True, else False is
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