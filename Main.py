def showbalance(Bal):
    print(f"Your balance is ${Bal:.2f}")

def deposit():
    pass

def withdraw():
    pass

balance = 0

IsRunning = True

while IsRunning:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Please enter your choice (1-4): ")
    if choice == "1":
        showbalance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        exit()
    else:
        print("That isn't a valid choice")