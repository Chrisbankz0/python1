def Task_one():
	print("Even numbers from 1-100: ")
	for number in range(1,101):
		if number % 2 == 0:
			print(number)
	print()

Task_one()


def Task_two():
	print("\nOdd numbers between 50 and 100: ")
	for number in range(50,101):
		if number % 2 == 1:
			print(number)
	print()

Task_two()


def Task_three():
	print("\nNumbers from 100 to 1: ")
	for number in range(100,0, -1):
		print(number)
	print()

Task_three()

def Task_four():
	print("\nSquares from 1 to 20: ")
	for number in range(1, 21):
		print(number * number)
	print()

Task_four()



def Task_five():
	print("\nMultiples of 3 between 1 and 50:")
	for num in range(1,51):
		if num % 3 == 0:
			print(num)
	print()

Task_five()



def Task_six():
	print("\nNumbers between 1-100 that are divisble by both 3 and 5")
	for num in range(1,101):
		if num % 3 == 0 and num % 5 == 0:
			print(num)
	print()

Task_six()


def Task_seven():
	sum = 0
	
	for num in range(1,101):
		if num % 7 == 0:
			sum+=1
	print("\nCount of numbers divisible by 7 between 1 and 100:")
	print(sum)
	print()

Task_seven()


def Task_eight():
    total = 0
    for num in range(1, 51):
        total += num
    print("\nSum of first 50 natural numbers:")
    print(total)

Task_eight()


def Task_nine():
    product = 1
    for num in range(1, 11):
        product *= num
    print("\nProduct of first 10 natural numbers =", product)

Task_nine()



def Task_ten():
    print("\nLetters A to Z")
    for alpha in range(65, 91):
        print(chr(alpha))

Task_ten()


def Task_eleven():
    num = 5
    print(f"\nMultiplication table of {num}")
    for multi in range(1, 13):
        print(f"{num} x {multi} = {num * multi}")

Task_eleven()

def Task_twelve():
    text = "Queen"
    print("\nCharacters in the string")
    for character in text:
        print(character)

Task_twelve()


def Task_thirteen():
    text = "Elephant never forgets"
    count = 0
    print("Count of letter 'e':")
    for ch in text:
        if ch == 'e' or ch == 'E':
            count += 1
    print(count)

Task_thirteen()


def Task_fourteen():
    text = "hello world"
    result = ""
    print("Lowercase to Uppercase:")
    for ch in text:
        if ch >= 'a' and ch <= 'z':
            ch = chr(ord(ch) - 32)
        result += ch
    print(result)

Task_fourteen()



def Task_fifteen():
    text = "HELLO WORLD"
    result = ""
    print("Uppercase to Lowercase:")
    for ch in text:
        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) + 32)
        result += ch
    print(result)

Task_fifteen()


def Task_sixteen():
    text = "Beautiful day"
    count = 0
    print("Number of vowels:")
    for ch in text:
        ch = ch.lower()
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1
    print(count)

Task_sixteen()


def Task_seventeen():
    number = 123456
    count = 0
    print("Count of digits:")
    for digit in str(number):
        count += 1
    print(count)

Task_seventeen()


def Task_eighteen():
    number = 12345
    total = 0
    print("Sum of digits:")
    for digit in str(number):
        total += int(digit)

    print(total)

Task_eighteen()


def Task_nineteen():
    number = 38527
    largest = 0
    print("Largest digit:")

    for digit in str(number):
        digit = int(digit)
        if digit > largest:
            largest = digit

    print(largest)

Task_nineteen()


def Task_twenty():
    number = 38527
    smallest = 9
    print("Smallest digit:")
    for digit in str(number):
        digit = int(digit)
        if digit < smallest:
            smallest = digit

    print(smallest)

Task_twenty()
