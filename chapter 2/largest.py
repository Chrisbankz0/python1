num1 = int(input("enter first number))
num2 = int(input("enter second number))
num3 = int(input("enter third number))

sum = num1 + num2 + num3
	print("the sum of all the numbers are ",sum)
average = sum/3
	print("The average is ",average)
product = num1*num2*num3
	print("The product of all the numbers are ",product)

	smallest = num1
if num2 < smallest:
	smallest = num2
if num3 < smallest:
	smallest = num3
	print(smallest, "is the smallest")

largest = num1
if num2 < largest:
	largest = num2
if num3 < largest:
	largest = num3
	print(largest, "is the largest")
