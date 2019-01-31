from team import Team
from player import Player

test_team = Team(0)
test_player = Player("John Doe", -1, -2)

def test_addPlayer():
    previous_players = test_team.players[:]
    test_team.addPlayer(test_player)
    assert not test_player in previous_players and test_player in test_team.players

# QUESTION: Probably not a good idea to have order matter with these tests?
def test_removePlayer():
    prev_playrs = test_team.players[:]
    test_team.removePlayer(test_player)
    assert test_player in prev_playrs and not test_player in test_team.players

def test_getId():
    assert test_team.getId() == 0

def test_getName():
    assert "0" == test_team.getName()

def test_contains():
    test_team.players.append(test_player)
    assert test_player in test_team

def test_isFull_teamOf5():
    # Get the length of the players list up to 5 so the team is one from full
    while len(test_team.players) < 5:
        test_team.players.append(test_player)

    # Players list should have 5, one from full
    assert not test_team.isFull()

def test_isFull_teamOf6():

    # Add one more player so the team is full
    test_team.players.append(test_player)
    assert test_team.isFull()

def test_isFull_teamOf7():

    # Add another player so the team is definately full
    test_team.players.append(test_player)
    assert test_team.isFull()
