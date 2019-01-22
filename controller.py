from roster import Roster
from player import Player
from team import Team


class Controller:

    def __init__(self):
        self.roster = None
        self.players_by_attack = []
        self.players_by_block = []
        self.teams = []

    def selectRoster(self, id):
        self.roster = Roster(id)
        # TODO what if id is out of range?

        # Get a copy of the players for each list
        self.players_by_attack = self.roster.getCopyOfPlayers()
        self.players_by_block = self.roster.getCopyOfPlayers()

        # Sort the lists by the appropriate stat, descending
        self.players_by_attack.sort(key=lambda player: player.attack_stat, reverse=True)
        self.players_by_block.sort(key=lambda player: player.block_stat, reverse=True)

    def getTop3Attackers(self):
        return self.players_by_attack[:3]

    def getTop3Blockers(self):
        return self.players_by_block[:3]

    def goAction(self, action_code):
        # Action 1 --> Return top 3 attackers
        # Action 2 --> Return top 3 blockers
        # Action 3 --> Return a list of an unknown number of teams TODO <--
        if action_code == 1:
            result = self.getTop3Attackers()
        elif action_code == 2:
            result = self.getTop3Blockers()
        elif action_code == 3:
            result = "UNSUPPORTED"

        return result

