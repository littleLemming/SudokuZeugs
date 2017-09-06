
class Solver:

    def __init__(self,  sudoku, line_len_sudoku, column_len_sudoku, csv, line_len_block, column_len_block):
        self.line_len_sudoku = line_len_sudoku
        self.column_len_sudoku = column_len_sudoku
        self.line_len_block = line_len_block 
        self.column_len_block = column_len_block
        if sudoku == None:
            self.sudoku = self.read_in(csv)
        else:
            self.sudoku = sudoku
        if not self.is_valid():
            raise Exception('InvalidSudoku', 'this sudoku is not valid - see error messages above')

    # solving a simple 9x9 sudoku
    def solve_9x9(self, sudoku):
        # find 0 - if no more can be found return sudoku
        # make list of numbers that could be filled in - if no numbers can be filled in, return 
        # call for every number solve_9x9 with copy of sudoku with one of those numbers
        for i in range(0,self.column_len_sudoku):
            if 0 in sudoku[i]:
                for j in range(0,self.line_len_sudoku):
                    possible = []
                    if sudoku[i][j] == 0:
                        for k in range(1, self.column_len_block*self.line_len_block + 1):
                            if k not in self.get_line(i) and k not in self.get_column(j) and k not in self.get_block(j,i,True):
                                possible.append(k)
                    print("i: " + str(i) + " j: " + str(j) + " val: " + str(sudoku[i][j]) + " possible: " + str(possible) + " line: " + str(self.get_line(i)) + " column: " + str(self.get_column(j)) + " block: " + str(self.get_block(j,i,True)))
        return sudoku


    # read in a csv as a sudoku
    def read_in(self, csv):
        pass

    # check if this sudoku is valid or if there are mistakes
    def is_valid(self):
        if self.column_len_sudoku != len(self.sudoku):
            return False
        for i in self.sudoku:
            if len(i) != self.line_len_sudoku:
                return False
        for i in range(0, self.column_len_sudoku):
            without_zero = list(filter(lambda x : x != 0, self.get_column(i)))
            if (len(without_zero) != len(set(without_zero))):
                return False
        for i in range(0, self.line_len_sudoku):
            without_zero = list(filter(lambda x : x != 0, self.get_line(i)))
            if (len(without_zero) != len(set(without_zero))):
                return False
        for i in range(0, self.column_len_sudoku, self.column_len_block):
            for j in range(0, self.line_len_sudoku, self.line_len_block):
                without_zero = list(filter(lambda x : x != 0, self.get_block(j, i, True)))
                if (len(without_zero) != len(set(without_zero))):
                    return False
        for i in sudoku:
            for j in sudoku:
                if j not in range(0, self.column_len_block*self.line_len_block + 1):
                    return False
        return True

    # def return the numbers of a line in a list - count starts at 0
    def get_line(self, line_nr):
        if line_nr < 0 or line_nr >= self.column_len_sudoku:
            raise Exception('OutsideOfSudoku', 'the requested spot lies outside of the bounds of the sudoku')
        return self.sudoku[line_nr]

    # def return the numbers of a line in a list - count starts at 0
    def get_column(self, column_nr):
        if column_nr < 0 or column_nr >= self.line_len_sudoku:
            raise Exception('OutsideOfSudoku', 'the requested spot lies outside of the bounds of the sudoku')
        return [x[column_nr] for x in self.sudoku]

    def get_block(self, x, y, regular_block):
        if y < 0 or y >= self.column_len_sudoku or x < 0 or x >= self.line_len_sudoku:
            raise Exception('OutsideOfSudoku', 'the requested spot lies outside of the bounds of the sudoku')
        # not yet implemented
        if not regular_block:
            return None
        num_block_line = int(x / self.line_len_block)
        num_block_column = int(y / self.column_len_block)
        list_list = ([x[num_block_line*self.line_len_block : num_block_line*self.line_len_block+self.line_len_block] for x in self.sudoku][num_block_column*self.column_len_block  : num_block_column*self.column_len_block +self.column_len_block])
        return ([x for sublist in list_list for x in sublist])


# some quick testing
# invalid sukdoku
#solver0 = Solver([[0,2,0,0,5,6,7,8,0],[2,0,0,5,0,7,8,9,1],[3,0,0,6,7,0,0,0,0],[4,0,6,7,0,0,0,2,3],[5,6,0,8,0,1,2,0,0],[6,0,0,9,0,2,0,4,0],[7,0,9,0,2,0,0,5,0],[8,0,0,2,0,4,0,6,0],[0,0,0,0,4,0,0,7,8]], 9, 9, None, 3, 3)
# valid sukokus
solver1 = Solver([[0,0,0,0,0,0,0,6,0],[0,2,3,0,6,0,4,5,1],[0,5,1,0,0,7,0,2,0],[0,0,0,6,0,8,5,0,0],[0,3,0,0,9,0,0,8,0],[0,0,5,7,0,3,0,0,0],[0,6,0,4,0,0,8,7,0],[1,8,2,0,7,0,3,4,0],[0,7,0,0,0,0,0,0,0]], 9, 9, None, 3, 3)
print(solver1.solve_9x9(solver1.sudoku))
#solver2 = Solver([[5,0,0,0,6,2,0,0,8],[0,0,0,0,4,0,9,0,0],[0,6,7,0,8,9,2,0,0],[4,0,5,0,0,0,0,0,0],[7,3,8,0,0,0,6,1,4],[0,0,0,0,0,0,3,0,2],[0,0,4,7,5,0,1,2,0],[0,0,1,0,2,0,0,0,0],[6,0,0,8,1,0,0,0,9]], 9, 9, None, 3, 3)
#solver3 = Solver([[4,0,0,0,3,2,6,0,0],[0,0,5,6,1,0,0,0,3],[0,0,0,0,0,0,0,7,0],[0,0,8,4,0,0,0,0,5],[7,0,1,0,0,0,0,0,0],[0,0,2,1,0,0,0,0,9],[0,0,0,0,0,0,0,2,0],[0,0,6,8,9,0,0,0,4],[9,0,0,0,6,3,5,0,0]], 9, 9, None, 3, 3)
#solver4 = Solver([[0,0,7,5,3,0,0,0,0],[0,0,0,8,0,0,7,0,0],[9,0,0,0,6,0,0,4,0],[3,1,0,0,0,0,0,0,0],[8,0,6,0,7,0,3,0,9],[0,0,0,0,0,0,0,1,8],[0,6,0,0,8,0,0,0,2],[0,0,9,0,0,1,0,0,0],[0,0,0,0,4,5,1,0,0]], 9, 9, None, 3, 3)

