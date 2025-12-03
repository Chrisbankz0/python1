weight = float(input("enter weight: "))
height = float(input("enter height: "))

bmi = weight/(height*height)

if(bmi <= 18.5):
	print("Underweight")
elif(bmi <=24.9):
	print("Normal")
elif(bmi <=29.9):
	print("Overweigt")
elif(bmi >=30):
	print("obese")
