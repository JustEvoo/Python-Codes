import random
import time


dice_art = {
    1: (
        "┌───────────┐",
        "│           │",
        "│     ●     │",
        "│           │",
        "└───────────┘"
    ),
    2: (
        "┌────────────┐",
        "│   ●        │",
        "│            │",
        "│        ●   │",
        "└────────────┘"
    ),
    3: (
        "┌───────────┐",
        "│  ●        │",
        "│     ●     │",
        "│        ●  │",
        "└───────────┘"
    ),
    4: (
        "┌───────────┐",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "└───────────┘"
    ),
    5: (
        "┌───────────┐",
        "│  ●     ●  │",
        "│     ●     │",
        "│  ●     ●  │",
        "└───────────┘"
    ),
    6: (
        "┌───────────┐",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "└───────────┘"
    )
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

#Adding the dices
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
print(dice)

#Dice display 1
#for die in range(num_of_dice):
    #for line in dice_art.get(dice[die]):
        #print(line)

#Dice display 2
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end =" ")
    print()

for die in dice:
    total += die


dots = "."
for i in range(1,10)
	dots = dots * (i%3+1)
	print(f"\rLoading{dots}", end=" ")
	time.sleep(0.5)

print(f"Total is: {total}")
