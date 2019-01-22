class Team:

    def __init__(self, name):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        self.players.remove(player)
