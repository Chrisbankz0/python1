total_bill = int(input("enter bill: "))

is_member = input("Are you a member?  (yes or no): ").lower()

if(total_bill >= 1000 and is_member == "yes"):
	print("10% off")

elif(total_bill >= 1000 and is_member == "no"):
	print("5% off")
else:
	print("nothing")

