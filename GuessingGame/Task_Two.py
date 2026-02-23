import random

answer = random.randint(1,10)
guess = int(input("Enter a random number: "))

if guess == answer:
	print(f"correct")
else:
	print("wrong Guess")
