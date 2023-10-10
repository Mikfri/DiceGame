#from Player import Player

class PlayerList:
    def __init__(self):
        self.playerList = []

    def addPlayer(self, player):
        self.playerList.append(player)

    def getPlayerList(self):
        return self.playerList

    def numPlayers(self):
        return len(self.playerList)



# if __name__ == "__main__" :
#     p1 = Player("Patrick", 5)
#     p2 = Player("Bob", 11)
#     p3 = Player("Squidward", 2)

#     playerList = PlayerList()
#     playerList.addPlayer(p1)
#     playerList.addPlayer(p2)
#     playerList.addPlayer(p3)

#     print(playerList)






        