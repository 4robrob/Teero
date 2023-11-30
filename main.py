# Teero 

import time
import sleep from time

# Var for Startingweapon
st.wep = input ("Do you want to have an easier experience?")

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
    else:
        return 0

# Calculate player's attack damage based on the chosen weapon
    def get_damage(self):
        base_damage = random.randint(10, 15)
        return base_damage + self.weapon_effect()




def intro ()
    print ("Welcome to Teero. This game is a textbased game so be prepaired to read a lot ^^")
    sleep (3)
    print ("So let us getting started")
    sleep (3)
    print (st.wep)
        if st.wep is any str (yes,yeah,y)
        set weapon = axe
        elif st.wep is any str (n,no,nah)
            return
        else 
            return
    print ("So you made your choice.")
    sleep (3)
    print ("")








# Function to initiate and control the gameplay
def play_game()
    weapon = st.wep
    player = Player (weapon)
    intro ()


#Start the game
play_game()
