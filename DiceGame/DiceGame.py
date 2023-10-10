from Die import Die         #Vi importere Die fordi vi i denne klasse opretter dem
#from Player import Player  #Vi opretter ikke Player herinde.. Importere vi den ikke - men referes
#from PlayerList import PlayerList
import time

class DiceGame:
    def __init__(self, playerList):
        self.die1 = Die("RedDie")       #Her oprettes 'terning #1' fra klassen Die
        self.die2 = Die("BluDie")       #Uden 'from Die import Die' ville vi ikke kunne oprette Dice objektet
        self.playerList = playerList    #Vi referere til spilleren.. men spilleren oprettes ikke her. Spilleren oprettes først i Main, hvorefter den referes til DiceGame..
    

    def rollDice(self, player):
        value1 = self.die1.roll()
        value2 = self.die2.roll()
        total_value = value1 + value2

        print(f"\nSooo.. {value1} + {value2} results in a total of: {total_value}")
        time.sleep(0.95)
        
        if total_value == 7:
            player.increaseScore() # Opdater spillerens score
            print(f"\n🅲 🅾  🅽 🅶 🆁 🅰  🆃 🆄 🅻 🅰  🆃 🅸 🅾  🅽 🆂 ❗\n")
            time.sleep(0.65)
            return f"   {player.name} now have {player.getScore()} point(s)!\n"
        else:
            print(f"\nSorry {player.name}..")
            time.sleep(0.9)
            print("No points for you..\n")
            time.sleep(1.2)
            return f"             ¯\_(ツ)_/¯\n"


    # def start():
    #     while True: #En evig løkke - indtil vi går ned af en gren (if-statement) som har et break-point
    #         try:
    #             playerAmount = int(input("Enter the number of players: "))
    #             if playerAmount < 1:
    #                 raise ValueError("Number of players must be at least 1")
    #             break  # (Else, underforstået..) Er 'playerAmount' over 1 = gyldig værdi > break! Vi går videre..
    #         except ValueError:
    #             print("Please enter a valid number of players.")

    #     #---: INDPUT SPILLER.NAVN(e) :---
    #     for i in range(playerAmount):   #For hver iteration(range) af 'playerAmount'.. skal der være en betingelse for 'i'...
    #         p_name = input(f"Enter the name of Player {i+1}: ")   #(fortsat).. i skal pluses med 1. Derudover gemmes brugerens input i variablen 'p_name' 
    #         player = Player(p_name)
    #         playerList.addPlayer(player)

    #     print("\nLet's begin!\n")

    #     # Løkke for at fortsætte spillet
    #     while True:
    #         # Loop gennem spillere og lad dem spille efter tur
    #         for player in playerList.getPlayerList():
    #             print(f"It's {player.name}'s turn.")
    #             input("Press Enter to roll the dice...")
        
    #             # Start spillet for den aktuelle spiller
    #             callMethod_rollDice = game.rollDice(player)
    #             print(callMethod_rollDice)

    #         # Vis pointstatusen for hver spiller
    #         print("\n---:POINT STATUS:---")
    #         for player in playerList.getPlayerList():
    #             print(f" {player.name}: {player.getScore()} point(s)")

    #         # Spørg om spillet skal fortsætte
    #         continueOption = input("\nDo you want to play another round? 'y/n': ")
    #         if continueOption.lower() != "y":
    #             print("Thanks for playing!")
    #             print(logo)
    #             break