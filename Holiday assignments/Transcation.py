balance = 0
transactions = []
count = -1

def deposit(balance, transactions):

	amount = int(input("Enter amount to deposit: "))
	if amount <= 0:
		print("Invalid amount")
		return balance, transactions

	balance += amount

	record = f"Deposited: ${amount} | New balance: {balance}"

	transactions.append(record)
	print("Deposit successful")
	print(record)

	return balance, transactions

def withdraw(balance, transactions):

	amount = int(input("enter amount to withdraw: "))

	if amount <= 0:
		print("Invalid amount")
		return balance, transactions


	if (amount > balance):
		print("insufficent funds")
		return balance, transactions

	balance -= amount

	record = f"withdrawn: ${amount} | New balance: ${balance}"

	transactions.append(record)
	print("\nwithdrawal successful")
	print(record) 

	return balance, transactions

def show_transactions(transactions):
	if len(transactions) == 0:
		print("No transactions yet")

	for number in range(len(transactions)):
		print(number + 1, "." , transactions[number])

while count != 0 :
	print("\nWelcome to the transaction log app")
	print("1. Deposit funds")
	print("2. Withdraw funds")
	print("3. Show Transactions")
	print("4. Exit")

	choice = input("\nEnter your choice(1-4): ")


	match choice:

		case "1":
			balance, transactions = deposit(balance, transactions)

		case "2":
			balance, transactions = withdraw(balance, transactions)

		case "3":
			show_transactions(transactions)

		case "4":
			print("The final balance is: ",balance)
			show_transactions(transactions)
			print("Thank you for using the Transaction Log app")
			count = 0

		case _:
			print("Invalid choice! please enter 1-4")

