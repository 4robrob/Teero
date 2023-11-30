import time

def intro():
    print("Welcome to Teero, the text-based adventure game!")
    time.sleep(1)
    print("You find yourself standing at a crossroad.")
    time.sleep(1)
    print("Where would you like to go?")
    time.sleep(1)

def crossroad():
    print("You're at a crossroad.")
    time.sleep(1)
    print("To your left is a dark forest.")
    time.sleep(1)
    print("To your right is a small village.")
    time.sleep(1)
    print("Where would you like to go? (left/right)")

def forest():
    print("You enter the dark forest.")
    time.sleep(1)
    print("You encounter a giant spider!")
    time.sleep(1)
    choice = input("What do you want to do? (fight/run)").lower()
    if choice == "fight":
        print("You defeated the spider! You're a brave hero.")
    else:
        print("You ran away, narrowly escaping the spider.")

def village():
    print("You arrive at the village.")
    time.sleep(1)
    print("You see a bustling marketplace.")
    time.sleep(1)
    print("You also notice a quiet inn.")
    time.sleep(1)
    choice = input("Where would you like to go? (market/inn)").lower()
    if choice == "market":
        print("You explore the market and find useful supplies.")
    else:
        print("You rest at the inn, feeling refreshed.")

def play_game():
    intro()
    crossroad()
    direction = input().lower()
    if direction == "left":
        forest()
    elif direction == "right":
        village()
    else:
        print("Invalid choice. Please try again.")

# Start the game
play_game()
