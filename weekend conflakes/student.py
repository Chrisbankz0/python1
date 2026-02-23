passes = 0
fails = 0

for student in range (15):
	user = int(input(f"enter score{student+1}: "))
	if user >= 65:
		passes += 1
	else:
		fails += 1


print("passes:", passes)
print("fails:", fails)