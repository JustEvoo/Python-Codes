import time

print("="*100)
print(f"{'WELCOME':^100}")
print("="*100)

carts = []
prices = []
total = 0
#add items
while True:
    cart = input("Enter food (q to quit): ")
    if cart.lower() == "q":
        break
    else:
        carts.append(cart)
        price = float(input("Enter price: $"))
        prices.append(price)
        total += price
#Verify items
print("=" * 100)
print("Please check your item/s")
print(f"your cart:", end=" ")
for cart in carts:
    print(f"{cart}, ", end=" ")
print()
verify = input("Proceed? (y/n): ")
if verify == "y":
    symbols = (" /", "--", " \\", " |", ' /')
    for i in symbols:
        text = f"Loading... {i}"
        print(f"\r{text}", end="")
        time.sleep(0.4)
    print()
    print(f"your total is ${total:,.2f}")
else:
    print(f"Please restart the program")








