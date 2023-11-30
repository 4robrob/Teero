# Teero 
# git add .
# git commit -m "<Description>"
# git push

#test


from time import sleep
import random
st_wep = None

class Player:
    def __init__(self, weapon):
        self.hp = 100
        self.items = []  # Player's inventory for items
        self.weapon = weapon  # Player's chosen weapon

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, amount):
        self.hp += amount


# Define weapon effects on damage
def weapon_effect(self):
    if self.weapon == "sword":
        return 8
    elif self.weapon == "axe":
        return 9
    elif self.weapon == "staff":
        return 4
    elif self.weapon == "wood sword":
        return 3
    elif self.weapon == "rocks":
        return 2
    elif self.weapon == "dust":
        return 1
    elif self.weapon == "bleeding hands":
        return -1
    else:
        return 0

# Calculate player's attack damage based on the chosen weapon
def get_damage(self):
    base_damage = random.randint(10, 15)
    return base_damage + self.weapon_effect()

def intro ():
    print ("Welcome to Teero. This game is a textbased game so be prepaired to read a lot ^^")
    sleep (3)
    print ("So let us getting started")
    sleep (3)
    # Var for Startingweapon
    global st_wep
    st_wep = input ("Do you want to have an easier experience? \n")
    if st_wep.lower() in ["yes","yeah","y"]:
        player = Player("axe")  # Creating the player instance with an initial weapon
    elif st_wep.lower () in ["n","no","nah"]:
        player = Player("")  # Creating the player instance with an initial weapon
        return
    else:
        print ("Invalide argument. Try again with y; yes; yeah or n; no; nah.")
        player = None 
        return
    if player:
        print ("So you made your choice.")
        sleep (3)
    
    








# Function to initiate and control the gameplay
def play_game():
    weapon = st_wep
    player = Player (weapon)
    intro ()


#Start the game
play_game()
