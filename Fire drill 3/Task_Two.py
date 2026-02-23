score = []
number = 0

def scores(number):
	for num in range(1,11):
		number = int(input("Enter scores: "))
		score.append(number)
	total = 0
	for item in score:
		if item % 2 == 1:
			total+=item
		
	print(total)


scores(number)