import random

books = ["The Strongman", "The Babydaddy", "The Lionheart", "The Nigerian", "The Twat"]

def show_menu():
	print("Welcome to the book Suggestion System")
	print("1. Get Suggestions")
	print("2. Add Book")
	print("3. Remove Book")
	print("4. Update Book")
	print("5. Show all Books")
	print("6. Exit")

def suggest_book():
	while True:
		book = random.choice(books)
		page = random.randint(1,20)

		print("Book for the day:")
		print(f"Book Title:{book}",)
		print(f"page:{page}")

		choice = input("Would you like another suggestion? (yes/no): ").lower()
		if choice != "yes":
			break

def add_book():
	while True:
		book = input("Enter the new book title: ")
		if book not in books:
			books.append(book)
			print("Book Added Sucessfully")
		else:
			print("Book already Exist")

def remove_book():
	while True:
		book = input("Enter book title to remove: ")
		if book in books:
			books.remove(book)
			print("Book Removed Sucessfully")
		else:
			print("Book doesn't Exist")

def update_book():
	while True:
		old_book = input("Enter the old book title: ")

		if old_book in books:
			new_book = input("Enter the new book Title: ")

			for book in range(len(books)):
				if books[book] == old_book:
					books[book] = new_book
					break
			print("Book Updated Sucessfully")
		else:
			print("Book doesn't Exist")

def show_books():
		if len(books) == 0:
			print("No Book Available")
		else:
			print("All Books")
			for book in range(len(books)):
				print(book + 1, ".", books[book])

while True:
	show_menu() 
	choice = input("Enter your choice (1-4): ")
	
	print()

	if choice == "1":
		 suggest_book()

	elif choice == "2":
		 add_book()

	elif choice == "3":
		 remove_book()

	elif choice == "4":
		 update_book()

	elif choice == "5":
		 show_books()

	elif choice == "6":
		break

	else:
		print("Invalid choice! Choose (1-4)")

	print()



