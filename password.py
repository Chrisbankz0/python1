password = str(input("enter name: "))

length = len(password)

if(length > 10):
	print("strong password")
else:
	print("weak")