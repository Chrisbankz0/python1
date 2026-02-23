import random

answer = random.randint(1,10)
guesses = 1


while True:
	guess = int(input("Enter a random number: "))

	if guess == answer:
		print(f"you are correct, The right number is: {guess}")
		print(f"The number of guesses are: {guesses}")
		break
	else:
		print("You are wrong please guess again")
		guesses += 1
