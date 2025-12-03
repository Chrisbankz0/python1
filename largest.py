num1 = int(input("enter number one: "))
num2 = int(input("enter number one: "))
num3 = int(input("enter number one: "))

largest = num1

if(num2 > largest):
	largest = num2
if(num3 > largest):
	largest = num3

	print(largest, "is the largest number in the list")