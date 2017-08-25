
class Solver:

    def __init__(self,  sudoku, csv, line_len_block, column_len_block):
        if sudoku == None:
            self.sudoku = self.read_in(csv)
        else:
            self.sudoku = sudoku
        if not self.is_valid(self.sudoku):
            raise Exception('InvalidSudoku', 'this sudoku is not valid - see error messages above')
        self.line_len_sudoku = int(len(sudoku[0])/column_len_block * line_len_block)
        self.column_len_sudoku = len(sudoku)
        self.line_len_block = line_len_block 
        self.column_len_block = column_len_block


    # solving a simple 9x9 sudoku
    def solve_9x9(self, sudoku):
        # find 0 - if no more can be found return sudoku
        # make list of numbers that could be filled in - if no numbers can be filled in, return 
        # call for every number solve_9x9 with copy of sudoku with one of those numbers
        pass

    # read in a csv as a sudoku
    def read_in(self, csv):
        pass

    # check if this sudoku is valid or if there are mistakes
    def is_valid(self, sudoku):
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

    def get_block(self, line_nr, column_nr, regular_block):
        if line_nr < 0 or line_nr >= self.column_len_sudoku or column_nr < 0 or column_nr >= self.line_len_sudoku:
            raise Exception('OutsideOfSudoku', 'the requested spot lies outside of the bounds of the sudoku')
        # not yet implemented
        if not regular_block:
            return None
        amnt_blocks_line = self.line_len_sudoku / self.line_len_block
        amnt_blocks_column = self.column_len_sudoku / self.column_len_block
        num_block_line = int(line_nr / amnt_blocks_line)
        num_block_column = int(column_nr / amnt_blocks_column)
        print(num_block_line)
        print(num_block_column)



# some quick testing

solver0 = Solver([[1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],[4,5,6,7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]], None, 3, 3)
solver1 = Solver([[1,2,3,4,5,6],[2,3,4,5,6,1],[3,4,5,6,1,2],[4,5,6,1,2,3],[5,6,1,2,3,4],[6,1,2,3,4,5]], None, 3, 2)
solver1.get_block(0,0,True)