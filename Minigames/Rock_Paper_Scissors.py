import random

options = ("Rock", "Paper", "Scissor")

running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Please enter a rock, paper, or scissor: ").capitalize()

    print(f"Computer chose: {computer}")
    print(f"Player chose: {player}")

    if player == computer:
        print(f"It's a tie!")
    elif player == "Rock" and computer == "Paper":
        print(f"You win!")
    elif player == "Paper" and computer == "Rock":
        print(f"You lose!")
    elif player == "Rock" and computer == "Scissor":
        print(f"You win!")
    elif player == "Scissor" and computer == "Paper":
        print(f"You lose!")
    elif player == "Scissor" and computer == "Rock":
        print(f"You lose!")
    elif player == "Paper" and computer == "Scissor":
        print(f"You lose!")
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        running = False