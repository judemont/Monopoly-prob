import random
import matplotlib.pyplot as plt

cases = [0] * 40

POLICE_CASE = 30
PRISON_CASE = 10
CHANCE_CASES = [7, 22, 36, 2, 17, 33]
CHANCE_GOTO = [39, 0, 24, 11, 15, -3, 10, 0, 10, 1, "nearest_station"]
CHANCE_GOTO_PROB = 4375
GARE_CASES = [5, 15, 25, 35]

def getNextPosition(position):
    nextPosition = position
    diceResult = random.randint(2, 6) + random.randint(2, 6)
    nextPosition += diceResult
    if nextPosition >= 40:
        nextPosition = position - 40
    elif nextPosition == POLICE_CASE:
        nextPosition = PRISON_CASE
    elif nextPosition in CHANCE_CASES:
        if random.randint(0, 10000) <= CHANCE_GOTO_PROB:
            chance_card = random.choice(CHANCE_GOTO)
            if chance_card == "nearest_station":
                nextPosition = min(GARE_CASES, key=lambda x: (x - nextPosition) % 40)
            elif chance_card < 0:
                nextPosition = (nextPosition + chance_card) % 40
            else:
                nextPosition = chance_card


    return nextPosition

for l in range(1000000):
    position = 0

    for i in range(30):
        position = getNextPosition(position)
        cases[position] += 1


print(cases)
x = [i for i in range(40)]
plt.xticks(x)
plt.plot(x, cases)
plt.grid()
plt.show()