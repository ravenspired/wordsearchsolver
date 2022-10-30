# Python3 program to print all elements
# of given matrix in diagonal order


# Main function that prints given
# matrix in diagonal order

# Driver Code
puzzle = [['f', 'h', 'a', 'i', 'c', 'a', 'l', 'c', 'n', 't'], ['i', 'u', 'e', 'q', 'z', 'o', 'f', 'm', 'z', 'v'], ['t', 'd', 'g', 'v', 'v', 'h', 'r', 'z', 'd', 'p'], ['u', 'o', 'n', 'z', 'l', 't', 'i', 's', 'a', 's'], ['k', 'm', 'u', 'j', 'q', 'o', 'l', 'g', 'w', 'z'], ['k', 't', 'z', 't', 'u', 'b', 'x', 'r', 'a', 'k'], ['q', 'l', 'y', 'f', 'x', 'p', 'j', 'y', 'k', 'n'], ['w', 't', 'x', 'e', 'm', 'k', 'e', 'u', 'x', 'a'], ['u', 'p', 'k', 'n', 'o', 'b', 'a', 'e', 'l', 'e'], ['c', 'x', 'z', 'e', 'j', 'n', 'q', 'e', 'd', 'f']]



ROW = len(puzzle)
COL = len(puzzle[0])

print("looping through line in range 1-", ROW+COL)
for line in range(1, (ROW + COL)):
	print("line:",line)

	start_col = max(0, line - ROW)
	print("start_col",start_col)

	count = min(line, (COL - start_col), ROW)
	print("count", count)
	test_string = ""

	print("looping through j in range count:",count)
	for j in range(count):
		print("j:",j)
		print("letter at those params:"+ str(puzzle[min(0, line) - j - 1][start_col + j])+"and coords are",min(ROW, line) - j - 1,start_col + j)
		test_string += str(puzzle[min(ROW, line) - j - 1][start_col + j])


	print(test_string)

# This code is contributed by Nikita Tiwari.

