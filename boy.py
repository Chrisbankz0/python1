number1 = int(input("Enter first interger: "))
number2 = int(input("Enter second interger: "))
number3 = int(input("Enter third interger: "))

smallest = number1

if number2 < smallest:
	smallest = number2
if number3 < smallest:
	smallest = number3

print("the smallest number is", smallest)