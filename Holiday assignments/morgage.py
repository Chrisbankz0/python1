principal = float(input("Enter the principal amount: "))

interest = float(input("Enter the annual interest rate: "))

years = int(input("Enter the duration in years: "))

monthly_rate = interest / 100.0 / 12.0

number_of_payment = years * 12

factor = (1 + monthly_rate) ** number_of_payment


monthly_payment = principal * (monthly_rate * factor) / (factor - 1)

print(f"Your monthly payment is ${monthly_payment:,.2f}")