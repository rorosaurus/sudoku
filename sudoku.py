import sys

# Matrix of Sudoku Table
z = 0	# Default cell value
row1 = [z,z,z,z,z,z,z,z,z];
row2 = [z,z,z,z,z,z,z,z,z];
row3 = [z,z,z,z,z,z,z,z,z];
row4 = [z,z,z,z,z,z,z,z,z];
row5 = [z,z,z,z,z,z,z,z,z];
row6 = [z,z,z,z,z,z,z,z,z];
row7 = [z,z,z,z,z,z,z,z,z];
row8 = [z,z,z,z,z,z,z,z,z];
row9 = [z,z,z,z,z,z,z,z,z];
table = [row1,row2,row3,row4,row5,row6,row7,row8,row9];

# Validate Input (maybe later)
#def validate(i):
	#blah

# Show Table (lol does this even need to be a function?)
def showtable():
	print '\nCurrent Table (0 denotes empty cell)\n'
	print row1,'\n',row2,'\n',row3,'\n',row4,'\n',row5,'\n',row6,'\n',row7,'\n',row8,'\n',row9,'\n',	# Print each row on a new line

# Enter/Set a Value (lol does this even need to be a function?)
def setvalue(r,c,n):
	table[r-1][c-1] = n

# Solve
def solve():
	skipped = 0
	blank = 0
	for row in range(0,9):
		for col in range(0,9):
			number = [False,False,False,False,False,False,False,False,False];
			if table[row][col] == 0:
				blank = blank + 1
				for rowx in range(0,9):	# Compare values from same row
					for num in range(1,10):
						if table[row][rowx] == num:
							number[num-1] = True
				for colx in range(0,9):	# Compare values from same column
					for num in range(1,10):
						if table[colx][col] == num:
							number[num-1] = True
				if row <= 2:	# Compare values from same box
					if col <= 2:
						for rowx in range(0,3):
							for colx in range(0,3):
								for num in range(1,10):
									if table[rowx][colx] == num:
										number[num-1] = True
					elif col <= 5:
						for rowx in range(0,3):
							for colx in range(3,6):
								for num in range(1,10):
									if table[rowx][colx] == num:
										number[num-1] = True
					elif col <= 8:
						for rowx in range(0,3):
							for colx in range(6,9):
								for num in range(1,10):
									if table[rowx][colx] == num:
										number[num-1] = True
				elif row <= 5:
					if col <= 2:
						for rowx in range(3,6):
							for colx in range(0,3):
								for num in range(1,10):
									if table[rowx][colx] == num:
										number[num-1] = True
					elif col <= 5:
						for rowx in range(3,6):
							for colx in range(3,6):
								for num in range(1,10):
									if table[rowx][colx] == num:
										number[num-1] = True
					elif col <= 8:
						for rowx in range(3,6):
							for colx in range(6,9):
								for num in range(1,10):
									if table[rowx][colx] == num:
										number[num-1] = True
				elif row <= 8:
					if col <= 2:
						for rowx in range(6,9):
							for colx in range(0,3):
								for num in range(1,10):
									if table[rowx][colx] == num:
										number[num-1] = True
					elif col <= 5:
						for rowx in range(6,9):
							for colx in range(3,6):
								for num in range(1,10):
									if table[rowx][colx] == num:
										number[num-1] = True
					elif col <= 8:
						for rowx in range(6,9):
							for colx in range(6,9):
								for num in range(1,10):
									if table[rowx][colx] == num:
										number[num-1] = True
				solvable = 0
				for num in range(0,9):	# Is this cell solvable?
					if number[num] == False:
						solvable = solvable + 1
				if solvable == 1:
					print '\nCell %sx%s is solvable!' % (row,col) # FINALLY actually solve here lolololol
					for num in range(0,9):
						if number[num] == False:
							table[row][col] = num + 1
				else:
					skipped = skipped + 1
	if blank > skipped:	# Iterates solver until table is completely solved or requires more cells to be filled
		solve()
	else:
		print '\nThe current table is as solved as possible.'

# Main Menu
def mainmenu():
	print "\nMain Menu\n","1 - Enter a Value\n","2 - Show Current Table\n","3 - Attempt to Solve\n","4 - Exit"
	menu = raw_input("Enter your selection: ")
	if int(menu) == 1:
		r = int(raw_input('Enter Row Number (1-9): '))		# Row input
		c = int(raw_input('Enter Column Number (1-9): '))	# Column input
		n = int(raw_input('Enter Cell Value (1-9): '))		# Cell value input
		setvalue(r,c,n)
		print '\n---'
		mainmenu()
	elif int(menu) == 2:
		showtable()			# Display the table
		print '\n---'
		mainmenu()
	elif int(menu) == 3:
		solve()
		print '\n---'
		mainmenu()
	elif int(menu) == 4:
		sys.exit(0)
	else:
		print 'Invalid input. Try again.'
		mainmenu()

mainmenu()