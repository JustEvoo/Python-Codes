import random
low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True
print("Welcome to the Number Guessing Game")
#Game
while is_running:
    guess = input("Please guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}")
        #hints
        elif guess > answer:
            print("Lower")
        elif guess < answer:
            print("Higher")
        else:
            print("Congratulations! You guessed the number!")
            is_running = False
    else:
        print(f"Please enter a number between {low} and {high}")
print("Thanks for playing!")





