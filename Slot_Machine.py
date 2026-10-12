def spin_row():
    pass
def print_row():
    pass
def get_payout():
    pass
def main():
    balance = 1000
    print("=" * 27)
    print("Welcome to the Slot Machine")
    print("Symbols: 🌸 👑 ⭐ 🍒")
    print("=" * 27)
    while balance > 0:
        print(f"Current balance: {balance}")
        bet = input("Please enter your bet: ")
        balance = balance - bet

if __name__ == "__main__":
    main()

