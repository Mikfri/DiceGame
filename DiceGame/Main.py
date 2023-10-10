from Player import Player
from DiceGame import DiceGame
from PlayerList import PlayerList

# Velkomst
print("\nWelcome to...")
logo = ("""                 the
 ██████╗░██╗░█████╗░███████╗░██████╗░░█████╗░███╗░░░███╗███████╗ 
 ██╔══██╗██║██╔══██╗██╔════╝██╔════╝░██╔══██╗████╗░████║██╔════╝
░██║░░██║██║██║░░╚═╝█████╗░░██║░░██╗░███████║██╔████╔██║█████╗░░
░██║░░██║██║██║░░██╗██╔══╝░░██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
 ██████╔╝██║╚█████╔╝███████╗╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
 ╚═════╝░╚═╝░╚════╝░╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
                                             by BobSponge
""")
print(logo)

#---: OPRET OBJEKTER :---
playerList = PlayerList()
game = DiceGame(playerList)

#---: INPUT ANTAL SPILLERE :----
#Antal spillere
while True: #En evig løkke - indtil vi går ned af en gren (if-statement) som har et break-point
    try:
        playerAmount = int(input("Enter the number of players: "))
        if playerAmount < 1:
            raise ValueError("Number of players must be at least 1")
        break  # (Else, underforstået..) Er 'playerAmount' over 1 = gyldig værdi > break! Vi går videre..
    except ValueError:
        print("Please enter a valid number of players.")

#---: INDPUT SPILLER.NAVN(e) :---
for i in range(playerAmount):   #For hver iteration(range) af 'playerAmount'.. skal der være en betingelse for 'i'...
    p_name = input(f"Enter the name of Player {i+1}: ")   #(fortsat).. i skal pluses med 1. Derudover gemmes brugerens input i variablen 'p_name' 
    player = Player(p_name)
    playerList.addPlayer(player)

print("\nLet's begin!\n")

# Løkke for at fortsætte spillet
while True:
    # Loop gennem spillere og lad dem spille efter tur
    for player in playerList.getPlayerList():
        print(f"It's {player.name}'s turn.")
        input("Press Enter to roll the dice...")
        
        # Start spillet for den aktuelle spiller
        callMethod_rollDice = game.rollDice(player)
        print(callMethod_rollDice)

    # Vis pointstatusen for hver spiller
    print("\n---:POINT STATUS:---")
    for player in playerList.getPlayerList():
        print(f" {player.name}: {player.getScore()} point(s)")

    # Spørg om spillet skal fortsætte
    continueOption = input("\nDo you want to play another round? 'y/n': ")
    if continueOption.lower() != "y":
        print("Thanks for playing!")
        print(logo)
        break