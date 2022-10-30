generate_size = int(input("What size? AxA, A?"))
import random

letters = "abcdefghijklmnopqrstuvwxyz"

puzzle = []



for x in range(generate_size):
	row_to_add = input("Please enter the row. Example: ailerghbgsr: ")
	puzzle.append(list(row_to_add))

# for x in range(generate_size):
# 	row_to_add = ""
# 	for y in range(generate_size):
# 		row_to_add += random.choice(letters) 
# 	puzzle.append(list(row_to_add))



print("Done. Printing array below.")
print(puzzle)