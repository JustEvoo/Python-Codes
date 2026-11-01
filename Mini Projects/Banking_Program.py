def show_balance(balance):
    print("=" * 27)
    print(f"Your balance is ${balance:.2f}")
    print("=" * 27)

def deposit():
    print("=" * 27)
    amount = float(input("Please enter the amount you want to deposit: "))
    print("=" * 27)
    if amount < 0:
        print("Sorry, you cannot deposit negative numbers")
        return 0
    else:
        return amount

def withdraw(balance):
    print("=" * 27)
    amount = float(input("Please enter the amount you want to withdraw: "))
    print("=" * 27)
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Sorry, you cannot withdraw negative numbers")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("=" * 27)
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("=" * 27)
        choice = input("Please enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            exit()
        else:
            print("That isn't a valid choice")

if __name__ == "__main__":
    main()