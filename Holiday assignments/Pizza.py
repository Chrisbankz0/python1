import math

pizza = print("""

Welcome to COHORT 29 pizza joint LEKKI BRANCH
_______________________________________________
Pizza type        number of Slices         Price per box
----------------------------------------------------------
1. SAPA SIZE              4                        2,000       
2. SMALL MONEY            6                        2,400      
3. BIG BOYS               8                        3,000      
4. ODOGWU                 12                       4,200      

""")


names = int(input("Enter the number of guest: "))
pizza = int(input("Enter pizza Choice: "))

match pizza:
	case 1:
		slice_per_box = 4
		price_per_box = 2000

	case 2:
		slice_per_box = 6
		price_per_box = 2400

	case 3:
		slice_per_box = 8
		price_per_box = 3000

	case 4:
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





