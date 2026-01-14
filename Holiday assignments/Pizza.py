import math

print("Welcome to Iya Scambirah pizza joint Ajegunle")
print("_______________________________________________")
print("Pizza type        number of Slices         Price per box")
print("----------------------------------------------------------")
print("Sapa Size              4                        2,000       ")
print("Small Money            6                        2,400       ")
print("Big Boys               8                        3,000       ")
print("Odogwu                 12                       4,200       ")


names = int(input("Enter the number of guest: "))
pizza_type = input("Enter pizza type: ").lower()

if pizza_type == "sapa size":
	slice_per_box = 4
	price_per_box = 2000

elif pizza_type == "small money":
	slice_per_box = 6
	price_per_box = 2400

elif pizza_type == "big boys":
	slice_per_box = 8
	price_per_box = 3000

elif pizza_type == "odogwu":
	slice_per_box = 12
	price_per_box = 4200

else:
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





