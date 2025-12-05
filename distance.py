distance = float(input("Enter the driving distance: "))
miles = float(input("Enter miles per gallon: "))
price = float(input("Enter price per gallon: "))

cost = distance/miles*price

print("The cost of driving is:$",round(cost, 2))