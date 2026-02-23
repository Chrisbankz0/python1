print("Back To Sender LLC")

successful_deliveries = int(input("Enter successful deliveries today: "))
base_pay = 5000

if successful_deliveries <= 0:
    print("Invalid amount! Deliveries cannot be negative.")

elif successful_deliveries < 50:
	amount_per_parcel = 160

elif successful_deliveries <= 59:
        amount_per_parcel = 200

elif successful_deliveries <= 69:
        amount_per_parcel = 250

else:
        amount_per_parcel = 500

days_wage = successful_deliveries * amount_per_parcel + base_pay

print(f"Total wage for today is {days_wage:,}")
