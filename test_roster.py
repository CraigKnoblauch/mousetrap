import sys, os, os.path
from roster import Roster

# Overkill way of figuring out how many rosters there are
num_rosters = len([roster for roster in os.listdir('.') if os.path.isfile(roster)])

# With this test, I want to make sure the list I have is truly a copy, not a reference
def test_getCopyOfPlayers():
    # I don't care what roster I get for this test. It's most likely there will always be at least one. So I just use
    # the first
    roster = Roster(1)
    some_players = roster.getCopyOfPlayers()
    some_players.pop()

    assert not some_players == roster.players

# TODO Make this flexible with an unknown number of rosters.



