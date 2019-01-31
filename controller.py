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

    def makeTeams(self):
        # For the number of teams of 6 possible, distribute the top players among these teams.
        num_players = self.roster.getNumPlayers()

        # Make an appropriate number of teams
        self.teams = [Team(team_number) for team_number in range(0, num_players//6)]

        # Blockers and Attackers of the same name exist in each list, thus we need to take
        # them from each list as we go.
        attacker = self.players_by_attack.pop(0)
        blocker  = self.players_by_block.pop(0)
        for i in range(0, 6//2):
            for team in self.teams:
                if not team.isFull():
                    # Confirm the attacker isn't in the team. This would happen if that player
                    # is there as a blocker role
                    while attacker in self.players_by_block:
                        self.players_by_block.remove(attacker)
                    team.addPlayer(attacker)

                    # Get another attacker for the next iteration of the loop
                    attacker = self.players_by_attack.pop(0)


                    # Do the same as we just did for attackers to blockers
                    while blocker in self.players_by_attack:
                        self.players_by_attack.remove(blocker)
                    team.addPlayer(blocker)

                    # Get another blocker for the next iteration of the loop
                    blocker = self.players_by_block.pop(0)




    def goAction(self, action_code):
        # Action 1 --> Return top 3 attackers
        # Action 2 --> Return top 3 blockers
        # Action 3 --> Return a list of an unknown number of teams TODO <--
        if action_code == 1:
            result = self.getTop3Attackers()
        elif action_code == 2:
            result = self.getTop3Blockers()
        elif action_code == 3:
            self.makeTeams()
            result = self.teams

        return result

