import random
import matplotlib.pyplot as plt

cases = [0] * 40

POLICE_CASE = 30
PRISON_CASE = 10
CHANCE_CASES = [7, 22, 36, 2, 17, 33]
CHANCE_GOTO = [39, 0, 24, 11, 15, -3, 10, 0, 10, 1, 100]
CHANCE_GOTO_PROB = 4375
GARE_CASES = [5, 15, 25, 35]

for l in range(100000):
    position = 0

    for i in range(30):
        diceResult = random.randint(2, 6) + random.randint(2, 6)
        position += diceResult
        if position >= 40:
            position = position - 40
        elif position == POLICE_CASE:
            position = PRISON_CASE
        elif position in CHANCE_CASES:
            if random.randint(0, 10000) <= CHANCE_GOTO_PROB:
                chanceCard = random.choice(CHANCE_GOTO)
                if chanceCard < 0:
                    position += chanceCard
                elif chanceCard == 100:
                    position = min(GARE_CASES, key=lambda x:abs(x-position))
                else:
                    position = chanceCard

        cases[position] += 1
print(cases)
x = [i for i in range(40)]
plt.xticks(x)
plt.plot(x, cases)
plt.grid()
plt.show()