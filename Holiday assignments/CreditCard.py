card = (input("Enter Credit Card Number: "))

length = len(str(card))
card_type = ""


if (length < 13 or length > 16):
	print("The card length is invalid")
else:
	print("The card length is valid")


if card.startswith("4"):
	cardType = "Visa card"

elif card.startswith("5"):
	cardType = "Mastercard"

elif card.startswith("37"):
	cardType = "American Express card"

elif card.startswith("6"):
	cardType = "Discover card"

else: 
	cardType = "Invalid Card"

print("The card type is: ", cardType)
print("The card length is: ", length)


total = 0
count = 0

for digit_char in reversed(card):
    digit = int(digit_char)

    if count == 0:
        digit *= 2
        if digit > 9:
            digit -= 9

    total += digit
    count = (count + 1) % 3 


if total % 10 == 0:
    print("Credit card is VALID")
else:
    print("Credit card is INVALID")
