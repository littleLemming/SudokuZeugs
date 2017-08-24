
# solving a simple 9x9 sudoku
def solve_9x9(sudoku):
    # find 0 - if no more can be found return sudoku
    # make list of numbers that could be filled in - if no numbers can be filled in, return 
    # call for every number solve_9x9 with copy of sudoku with one of those numbers