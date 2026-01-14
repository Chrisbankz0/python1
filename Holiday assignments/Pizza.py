import math

pizza = print("""

print("Welcome to COHORT 29 pizza joint LEKKI BRANCH")
print("_______________________________________________")
print("Pizza type        number of Slices         Price per box")
print("----------------------------------------------------------")
print("SAPA SIZE              4                        2,000       ")
print("SMALL MONEY            6                        2,400       ")
print("BIG BOYS               8                        3,000       ")
print("ODOGWU                 12                       4,200       ")

""")


names = int(input("Enter the number of guest: "))
pizza = input("Enter pizza type: ").upper()

match pizza:
	case "SAPA SIZE":
		slice_per_box = 4
		price_per_box = 2000

	case "SMALL MONEY":
		slice_per_box = 6
		price_per_box = 2400

	case "BIG BOYS":
		slice_per_box = 8
		price_per_box = 3000

	case "ODOGWU":
		slice_per_box = 12
		price_per_box = 4200

	case _:
		print("Invalid pizza type")
		exit()


boxes = math.ceil(names / slice_per_box)

total_slice = boxes * slice_per_box
leftover_slices = total_slice - names
total_price = boxes * price_per_box

print()

print(f"The number of boxes to buy is: {boxes} boxes")

print(f"The leftover slice is {leftover_slices} slices")

print(f"The price of total pizza {total_price:,}")





