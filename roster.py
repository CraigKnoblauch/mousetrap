from player import Player
import os


class Roster:

    def __init__(self, id):
        self.id = id
        self.players = []
        self.__setPlayers()

    def __setPlayers(self):
        # Open roster{id}.txt and parser with ' ' as a delimter. Items are name, attack, block
        roster_filename = "rosters/roster{}.txt".format(self.id)
        with open(roster_filename, 'r') as f:
            for line in f.readlines():
                stats = line.strip().split(' ')
                curr_player = Player(stats[0], stats[1], stats[2])
                self.players.append(curr_player)

    def getCopyOfPlayers(self):
        return self.players[:]

