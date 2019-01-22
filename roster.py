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

                name = "{} {}".format(stats[0], stats[1])
                attack_stat = stats[2]
                block_stat = stats[3]

                curr_player = Player(name, attack_stat, block_stat)
                self.players.append(curr_player)

    def getCopyOfPlayers(self):
        return self.players[:]

