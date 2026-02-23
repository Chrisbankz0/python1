import random

answer = random.randint(1,10)

guess = int(input("Enter a random number: "))


if guess == answer:
	print(f"you are correct, The right number is: {guess}")
	print(f"The number of guesses are: {guesses}")
else:
	if guess > answer:
		print("Too High")

	elif guess < answer:
		print("Too Low")
	
	elif guess != answer:
		print("You are wrong please guess again")