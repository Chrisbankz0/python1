
num = int(input("enter number: "))

for number in range (1, 11):
	result = f"{num} x {number} = {"":>6}{num * number}"
	print(result)