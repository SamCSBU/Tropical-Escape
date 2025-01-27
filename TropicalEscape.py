# TropicalEscape.py
# By SamCSBU

# define initial variables
choice = 1
location = 1
inventory = []
itemPresent = ""
gotSword = "no"
tigerAlive = "yes"
telescopePirateDead = "no"
swordGround = "yes"
grenadeGround = "yes"
# game over function, used when the user dies
def gameOver():
    print("")
    print("You died! Better luck next time!")
# win function, used when the player reaches the goal
def youWin():
    print("Congratulations! You got past the pesky pirates!")
    print("You take a map from the pirates and sail away on their ship.")
# carry function, used when the player says 'carry' and an item is present
def carry(itemPresent):
    item = input("Carry what? ")
    item = item.lower()
    if item == itemPresent:
        print("You are now carrying a",itemPresent)
        inventory.append(itemPresent)
        if item == "sword":
            global gotSword
            gotSword = "yes"
            global swordGround
            swordGround = "no"
        elif item == "grenade":
            global grenadeGround
            grenadeGround = "no"
    else:
        print("I don't know what you mean.")
      
# introduction
print("Welcome to the ADVENTURE GAME! \n")
while choice != "yes" and choice != "no": # keeps asking if user wants instructions if user does not respond with yes or no
    choice = input(str("Would you like instructions? "))
    choice = choice.lower()
    if choice != "yes" and choice != "no":
        print("Please answer with 'yes' or 'no'")
# give instructions if user says yes
if choice == "yes":
    print("You are stranded on a desolate island, in the middle of the sea.\n")
    print("Say 'inventory' to check what you may be carrying. \n")
    print("To move, say 'w' for west, 'n' for north, 'e' for east, and 's' for south. \n")
    print("Say 'carry' if you want to pick something up. \n")
    print("I am afraid that is all I can tell you. Off you go on your way. \n")

print("You are in the edge of an island. The rough ocean waves stop you from swimming out to sea.")
while location != 15:
    print("")
    answer = input("What do you want to do now? ") # asks user what they want to do each time
    answer = answer.lower() # make input not case sensitive
    if answer != "inventory" and answer != "n" and answer != "e" and answer != "s" and answer != "w" and answer != "carry":
        print("I don't know what that means")
    elif answer == "inventory":
        print("You are carrying",inventory)
    elif location == 1:
        if answer == "n":
            print("You are on the edge of the shore. You do not have a way to cross.")
        if answer == "e":
            if tigerAlive == "yes":
                print("You are in a bright forest. You hear the loud growls of an animal in the distance.")
                location = 2
            else:
                print("You are in a bright forest. It seems eerily quiet.")
                location = 2
        if answer == "s":
            print("You walk across the sandy shore of the island. A pirate ship is in the distance.")
            location = 4
        if answer == "w":
            print("You are on the edge of the shore. You do not have a way to cross.")
        if answer == "carry":
            print("There is nothing around to pick up.")
    elif location == 2:
        if answer == "n":
            print("The towering palm trees block your way.")
        if answer == "e":
            if tigerAlive == "yes":
                if gotSword == "no":
                    print("You move deeper into the forest, surrounded by a panda's favorite snack. The growls grow even louder. A rusty old sword lays nearby.")
                    location = 3
                else:
                    print("You move deeper into the forest, surrounded by a panda's favorite snack. The growls grow even louder.")
                    location = 3
            else:
                print("You move deeper into the forest, which seems suspiciously quiet.")
                location = 3
        if answer == "s":
            print("You are now in a swampy part of the forest, inhabited by orange frogs, large flamingoes, and insects buzzing everywhere.")
            location = 5
        if answer == "w":
            print("You are in the edge of an island. The rough ocean waves stop you from swimming out to sea.")
            location = 1
        if answer == "carry":
            print("There is nothing around to pick up.")
    elif location == 3:
        if answer == "n":
            print("The massive wall of bamboo trees prevent you from venturing that way.")
        if answer == "e":
            print("The massive wall of bamboo trees prevent you from venturing that way.")
        if answer == "s":
            if tigerAlive == "yes":
                print("You are now in a cave, inhabited by a large, white bengal tiger. It stares you right in the eyes.")
                location = 6
            elif tigerAlive == "no":
                print("You are in the tiger's cave. Its bloody, dead body lays in the middle of it.")
                location = 6
        if answer == "w":
            if tigerAlive == "yes":
                print("You are in a bright forest. You hear the loud growls of an animal in the distance.")
                location = 2
            else:
                print("You are in a bright forest. It is strangely quiet.")
                location = 2
        if answer == "carry":
            if swordGround == "yes":
                itemPresent = "sword"
                carry(itemPresent)
            elif swordGround == "no":
                print("There is nothing around to pick up.")
    elif location == 4:
        if answer == "n":
            print("You are in the edge of an island. The rough ocean waves stop you from swimming out to sea.")
            location = 1
        if answer == "e":
            print("The enormous palm trees of the forest prevent you from entering it.")
        if answer == "s":
            print("You are now at a corner of the island. A large pirate ship has washed up on shore. It is too tall is climb, however.")
            location = 7
        if answer == "w":
            print("You are on the edge of the shore. You do not have a way to cross.")
        if answer == "carry":
            print("There is nothing around to pick up.")
    elif location == 5:
        if answer == "n":
            if tigerAlive == "yes":
                print("You are in a bright forest. You hear the loud growls of an animal in the distance.")
                location = 2
            else:
                print("You are in a bright forest. It seems eerily quiet.")
                location = 2
        if answer == "e":
            print("The rocky exterior of the cave is impossible to get through this way.")
        if answer == "s":
            if telescopePirateDead == "no":
                print("You exit the forest and see a pirate with a telescope, looking outward at the sea. He does not seem to notice you.")
                location = 8
            else:
                print("You exit the forest, now along the shore. The dead body of the pirate lays at the water's edge.")
                location = 8
        if answer == "w":
            print("The giant palm trees prevent you from exiting the forest this way.")
        if answer == "carry":
            print("There is nothing around to pick up.")
    elif location == 6:
        if answer == "n":
            if tigerAlive == "yes":
                if gotSword == "no":
                        print("You run away from the tiger, but it chases you. You are surrounded by bamboo trees and the tiger catches up to you, slashing through your torso.")
                        gameOver() #Ending #6 - try to escape tiger north, no sword
                        break
                else: #Tiger Death #1
                    if inventory.count("grenade") == 0:
                        print("The tiger jumps at you as you run away. You hold out your sword, and it impales the tiger right through the stomach. Your sword remains stuck in its body, but the tiger is dead.")
                        inventory.remove("sword")
                        gotSword = "no"
                        tigerAlive = "no"
                        location = 3
                    else:
                        print("The tiger jumps at you as you run away. You hold  out your sword, and it impales the tiger right through the stomach, but not before it manages to get a claw on your grenade.")
                        gameOver() #ENDING 10 - try to escape tiger north with a sword, a grenade
                        break
            else:
                print("You exit the cave, and are surrounded by a panda's favorite snack.")
                location = 3
        if answer == "e":
            if tigerAlive == "yes":
                print("You are surrounded by the cave walls. The tiger continues to stare into your soul.")
            else: print("The cave walls block you from going this way.")
        if answer == "s":
            if gotSword == "no":
                if inventory.count("grenade") == 0:
                    if tigerAlive == "yes":
                        print("You attempt to slowly sneak past the white tiger. It respects your courage and lets you pass. A band of pirates is sitting around a campfire. They see you are unarmed and immediately shoot at you with their pistols.")
                        gameOver() #ENDING 1 - visit pirates with no sword, no grenade, tiger ALIVE
                        break
                    elif tigerAlive == "no":
                        print("You exit the cave, and see a band of pirates sitting around a campfire. They attack you all at once with their knives.")
                        gameOver() #ENDING 2 - visit pirates with no sword, no grenade, tiger DEAD
                        break
                else: 
                    if tigerAlive == "yes":
                        print("You attempt to sneak past the tiger. It sees you clutching a grenade and it pounces on you.")
                        gameOver() #ENDING 3 - try to sneak past tiger with no sword, a grenade
                        break
                    elif tigerAlive == "no":
                        print("You exit the cave, and see a band of pirates sitting around a campfire. They start to get up to attack you, but you throw your grenade at them, killing them all.")
                        youWin() #ENDING 11 (GOOD ENDING) - visit pirates with no sword, a grenade, tiger DEAD
                        break
            elif gotSword == "yes":
                if inventory.count("grenade") == 0:
                    print("You attempt to sneak past the tiger, and as you walk past it, it sees the sword on your back. The tiger jumps at you from behind, killing you.")
                    gameOver() #ENDING #4 - try to sneak past tiger with a sword, no grenade
                    break
                else:
                    print("You attempt to sneak past the tiger, and as you walk past it, it sees the sword on your back. The tiger jumps at you from behind, activating the grenade.")
                    gameOver() #ENDING #5 - try to sneak past tiger with a sword, a grenade
                    break      
        if answer == "w":
            if tigerAlive == "yes":
                print("You are surrounded by the cave walls. The tiger continues to stare into your soul.")
            else: print("The cave walls block you from going this way.")
        if answer == "carry":
            print("There is nothing around to pick up.")
    elif location == 7:
        if answer == "n":
            print("You walk across the sandy shore of the island. A pirate ship is in the distance.")
            location = 4
        if answer == "e":
            if telescopePirateDead == "no":
                print("You see a pirate looking out at sea with a nifty little telescope. He does not seem to notice you. ")
                location = 8
            else:
                print("You continue along the shore. The dead body of the pirate lays near the water.")
                location = 8
        if answer == "s":
            print("The pirate ship blocks you from going that way. ")
        if answer == "w":
            print("You cannot go this way, as you are on the edge of the island.")
        if answer == "carry":
            print("There is nothing around to pick up.")
    elif location == 8:
        if answer == "n":
            print("You enter a swampy part of the forest, inhabited by orange frogs, large flamingoes, and insects buzzing everywhere.")
            location = 5
        if answer == "e":
            if telescopePirateDead == "no":
                print("You see a band of pirates sitting around a campfire. The pirate with the telescope now notices you. He comes up from behind and hits you in the head with his telescope.")
                gameOver() #ENDING 8 - visit pirates from location 8, telescopePirate ALIVE
                break
            else:
                print("You see a band of pirates sitting around a campfire. One pirate from a watchtower sees you, and fires a cannonball at you.")
                gameOver() #ENDING 9 - visit pirates from location 8, telescope pirate DEAD
                break
        if answer == "s":
            if telescopePirateDead == "no":
                if gotSword == "no":
                    print("You walk up to the pirate with the telescope. He hears your footsteps and throws a knife at you, which hits you in the eyeball.")
                    gameOver() #ENDING 7 - approach telescope pirate, no sword 
                    break
                elif gotSword == "yes":
                    print("You walk up to the pirate with the telescope. He hears your footsteps and throws a knife at you, which you deflect with your sword. You then stab the pirate in the stomach. He dies, dropping a grenade.")
                    telescopePirateDead = "yes"
            elif telescopePirateDead == "yes":
                print("The edge of the ocean prevents you from exploring further this way.")
        if answer == "w":
            print("You are now at a corner of the island. A large pirate ship has washed up on shore. It is too tall is climb, however.")
            location = 7
        if answer == "carry":
            if telescopePirateDead == "no":
                print("There is nothing around to pick up")
            elif telescopePirateDead == "yes" and grenadeGround == "yes":
                itemPresent = "grenade"
                carry(itemPresent)
            elif telescopePirateDead == "yes" and grenadeGround == "no":
                print("There is nothing around to pick up. The dead body of the pirate lays nearby.")
