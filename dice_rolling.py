import random


nextRoll = True
while nextRoll != False:
    diceResult = random.randint(1, 6)
    diceRoll = input(
        "Do you want to roll the dice? Press (Y) for YES and anything else for NO ").lower()
    if diceRoll == "y":
        print(f"Result: {diceResult}")
    else:
        print("Bye, bye! Have a nice day!")
        nextRoll = False
