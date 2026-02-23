import random

answer = random.randint(1,10)
guesses = 1


while True:
	guess = int(input("Enter a random number: "))

	if guess == answer:
		print(f"you are correct, The right number is: {guess}")
		print(f"You won in {guesses} attempts.")
		break
	else:
		if guesses > 10:
			print("Game Over")
			print(f"The correct guess is {answer}")
			break

		else:
			print("You are wrong please guess again")
		guesses += 1

		