# solves a standard 9x9 sudoku input via a file where every line contains 9 ints spereated by one space, ints in range 0-9 where 0 stands for an empty spot
# this file contains different algorithms to solve such a sudoku

import sys

def read_in(file_name):
	with open(file_name) as f:
		sudoku_in = f.readlines()
	str = ''
	if len(sudoku_in) != 9:
		str += 'the sudoku has to be exactly 9 lines long\n'
	sudoku = []
	for i in sudoku_in:
		try:
			line = list(map(int,i.split()))
			if len(line) != 9:
				str += 'one line needs to be exactly 9 ints long\n'
			for i in line:
				if i < 0 or i > 9:
					str += 'the ints need to be between 0 and 9 inclusive\n'
					break
			sudoku.append(line)
		except:
			str += 'the sudoku needs to consists of only ints\n'
			break
	if str != '':
		raise Exception(str)
	return sudoku



def main():
	if len(sys.argv)== 2:
		sudoku = read_in(sys.argv[1])
	else:
		sudoku = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
	print(sudoku)

if __name__ == '__main__':
	main()


