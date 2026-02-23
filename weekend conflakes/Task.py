def Task_one():
	string = "house"
	reversed = ""

	print("Reverse of string:")
	for num in range(len(string) -1, -1, -1):
		reversed += string[num]
	print(reversed)

Task_one()

def Task_two():
	string = 12345
	reversed = ""

	print("Reverse of number:")
	for num in str(string):
		reversed = num + reversed
	print(reversed)

Task_two()

def Task_three():
	string = "HouSe"
	count = 0

	print("Count of uppercase letters:")
	for num in string:
		if num >= 'A' and num <= 'Z':
			count +=1
	print(count)

Task_three()

def Task_four():
	string = "HouSe"
	count = 0

	print("Count of lowercase letters:")
	for num in string:
		if num >= 'a' and num <= 'z':
			count +=1
	print(count)

Task_four()

def Task_five():
	string = "HouSe"

	position = -1

	print("Position of first vowel:")

	for index in range(len(string)):
		character = string[index].lower()

		if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
			position = index
			break

	print(position +1)

Task_five()

def Task_six():
	textValue = "House"

	print("Characters with ASCII values:")

	for character in textValue:
		print(character, "=", ord(character))

Task_six()


def Task_seven():
	total = 0
	counted = 0

	print("Average of numbers from 1 to 100:")

	for num in range(1, 101):
		total += num
		counted += 1
	average = total / counted
	print(average)

Task_seven()


def Task_eight():
    numberValue = 12

    print("Divisors of", numberValue)

    for possibleDivisor in range(1, numberValue + 1):
        if numberValue % possibleDivisor == 0:
            print(possibleDivisor)

Task_eight()

def Task_nine():
    numberValue = 12
    divisorCount = 0

    print("Count of divisors of", numberValue)

    for possibleDivisor in range(1, numberValue + 1):
        if numberValue % possibleDivisor == 0:
            divisorCount += 1

    print(divisorCount)

Task_nine()

