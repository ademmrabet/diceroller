import random
from dice import dice_art

dice = []
total = 0
numOfDice = int(input("How many Dice?: "))

for die in range(numOfDice):
    dice.append(random.randint(1, 6))

for die in range(numOfDice):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total += die
print(f"total: {total}")