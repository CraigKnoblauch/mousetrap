class Player:

    def __init__(self, name, attack_stat, block_stat):
        self.name = name
        self.attack_stat = attack_stat
        self.block_stat = block_stat

    def setName(self, name):
        self.name = name

    def setAttackStat(self, attack_stat):
        self.attack_stat = attack_stat

    def setBlockStat(self, block_stat):
        self.block_stat = block_stat

    def __eq__(self, other):
        are_equal = self.name == other.name and self.attack_stat == other.attack_stat and self.block_stat == other.block_stat
        return are_equal

    def __str__(self):
        return self.name


