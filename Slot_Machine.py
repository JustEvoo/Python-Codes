import random


def spin_row():
    symbols = ['🌸', '👑', '⭐', '🍒']
    # method 1
    #results = []
    #for symbol in range(3):
    #    results.append(random.choice(symbols))
    #return results

    #method 2
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("=" * 13)
    print(" | ".join(row))
    print("=" * 13)
    print()

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 30
        elif row[0] == '⭐':
            return bet * 10
        elif row[0] == '👑':
            return bet * 40
        elif row[0] == '🌸':
            return bet * 20
    else:
        return 0
def main():
    balance = 1000
    print("=" * 27)
    print("Welcome to the Slot Machine")
    print("Symbols: 🌸 👑 ⭐ 🍒")
    print("=" * 27)
    #Balance Input
    while balance > 0:
        print(f"Current balance: {balance}")
        bet = input("Please enter your bet: ")
        if not bet.isdigit():
            print("Please enter a number")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost")

        balance += payout

        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("=========================================================")
    print(f"Thank you for playing! Your final balance is ${balance}")
    print("=========================================================")

if __name__ == "__main__":
    main()

