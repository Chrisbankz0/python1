balance = 0
transactions = []

def deposit():
	global balance, transactions

	amount = int(input("Enter amount to deposit: "))
	balance += amount
	record = f"Deposited: ${amount} | New balance: {balance}"

	transactions.append(record)
	print("Deposit successful")
	print(record)

def withdraw():
	global balance, transactions

	amount = int(input("enter amount to withdraw: "))

	if (amount <= balance):
		balance -= amount

		record = f"withdrawn: ${amount} | New balance: ${balance}"

		transactions.append(record)
		print("\nwithdrawal successful")
		print(record)
	else:
		print("insufficent funds")

def show_transactions():
	if len(transactions) == 0:
		print("No transactions yet")
	else:
		for number in range(len(transactions)):
			print(number + 1, "." , transactions[number])

while True:
	print("\nWwelcome to the transaction log app")
	print("1. Deposit funds")
	print("2. Withdraw funds")
	print("3. Show Transactions")
	print("4. Exit")

	choice = input("\nEnter your choice(1-4): ")

	if choice == "1":
		deposit()

	elif choice == "2":
		withdraw()

	elif choice == "3":
		show_transactions()

	elif choice == "4":
		print("The final balance is: ",balance)
		show_transactions()
		print("Thank you for using the Transaction Log app")
		break

	else:
		print("Invalid choice! please enter 1-4")

