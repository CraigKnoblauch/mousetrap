from player import Player

test_player = Player("John Doe", 1.00, 2.00)

def test_setName():
    previous_name = test_player.name
    test_player.setName(previous_name + "new")
    assert test_player.name == previous_name + "new"

    test_player.name = previous_name

def test_setAttackStat():
    previous_stat = test_player.attack_stat
    test_player.setAttackStat(previous_stat + 1)
    assert test_player.attack_stat == previous_stat + 1

    test_player.attack_stat = previous_stat

def test_setBlockStat():
    prev_stat = test_player.block_stat
    test_player.setBlockStat(prev_stat + 1)
    assert test_player.block_stat == prev_stat + 1

    test_player.block_stat = prev_stat

def test_eq():
    identical_player = Player(test_player.name, test_player.attack_stat, test_player.block_stat)
    new_player = Player(test_player.name + "new", test_player.attack_stat + 1, test_player.block_stat + 1)

    assert identical_player == test_player
    assert not new_player == test_player

def test_str():
    string_player_name = test_player.name
    assert string_player_name == str(test_player)

def test_repr():
    string_player_name = test_player.name
    assert string_player_name == repr(test_player)
