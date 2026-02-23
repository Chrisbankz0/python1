
def taskthree():
	answer = random.randint(1,20)

		guess = int(input("Enter a random number: "))

		if guess > answer:
			print("Too High")
		elif guess < answer:
			print("Too Low")
		elif guess == answer:
			print(f"you are correct, The right number is: {guess}")
			print(f"The number of guesses are: {guesses}")
		else:
			print("You are wrong please guess again")



def taskfour():
	answer = random.randint(1,2)


	while True:
		guess = int(input("Enter a random number: "))

		if guess == answer:
			print(f"you are correct, The right number is: {guess}")
			print(f"The number of guesses are: {guesses}")
			break
		else:
			print("You are wrong please guess again")




def task_Six():
	answer = random.randint(1,2)
	guesses = 1


	while True:
		guess = int(input("Enter a random number: "))

		if guess == answer:
			print(f"you are correct, The right number is: {guess}")
			print(f"You won in {guesses} attempts.")
			break
		
		elif guesses > 10:
			print("Game Over")
			print("The correct guess is {answer}")
			break

		else:
			print("You are wrong please guess again")
		guesses += 1

			




def main ():

	task_Six()

main()



	