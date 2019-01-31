class Team:

    def __init__(self, id):
        self.id = id
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        self.players.remove(player)

    def getId(self):
        return self.id

    def getName(self):
        return str(self.id)

    def __contains__(self, player):
        return player in self.players

    def isFull(self):
        return len(self.players) >= 6
