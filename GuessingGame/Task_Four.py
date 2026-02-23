import random
answer = random.randint(1,10)


while True:
	guess = int(input("Enter a random number: "))

	if guess == answer:
		print(f"you are correct, The right number is: {guess}")
		break
	else:
		print("You wrong please guess again")