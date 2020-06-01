import random
valid_input = ["roll 1, roll 2, quit"]

def get_dice():
    return input("roll 1 or roll 2: ")

while True:
    b = get_dice()
    if b == "quit":
        print("alright, thankyou for playing")
        break
    if b == "roll 1":
        print(random.sample(range(1, 7), 1))
    elif b == "roll 2":
        print(random.sample(range(1, 7), 2))
