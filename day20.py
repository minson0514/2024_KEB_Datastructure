import random

answer = random.randint(1, 100)
chance= 7

while chance != 0:
    guess = int(input("Enter guess number : "))
    if guess == answer:
        print(f"You win. Answer is {answer}.")
        break
    elif guess > answer:
        chance = chance -1
        print(f"{guess} is bigger than answer. Chance left: {chance}")
    else:
        chance = chance-1

        print(f"{guess} is smaller than answer. Chance left: {chance}")