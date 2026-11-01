
menu = {"Pizza": 3.50,
        "Burger": 4.50,
        "Pasta": 15.50,
        "Ice cream": 3.50,
        "Popcorn": 9.50,
        "Chips": 3.99}
cart = []
total = 0
#Menu Lists
print("=" * 100)
print(f"{"Welcome to the menu":^100}")
print("=" * 100)
for key, value in menu.items():
    print(f"{key:7}: ${value:.2f}")
print("-" * 100)
#Customer input
while True:
    food = input("Select an option (q to quit): ").capitalize()
    if food == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Invalid option, please try again.")
#Order overview
print("------------------ YOUR ORDER ------------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total is: ${total}")
#Payment Method
check = input("Do you want to check out your items? (y/n): ")
if check == "y":
    print("Please enter a payment method")
    payment_method = (("QRIS", "APPLE PAY", "GOPAY"),
                      ("DANA", "OVO", "SEABANK"))
    for row in payment_method:
        for pay in row:
            print(pay.capitalize(), end=" ")
        print()

    method = input("Enter your payment method: ").upper()
    valid = False
    for row in payment_method:
        if pay in row:
            valid = True
            break
    if valid:
        print(f"You have successfully paid your item/s using{method}")
else:
    print("Please go back and try again.")


