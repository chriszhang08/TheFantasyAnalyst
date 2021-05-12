# store scores by team, indexed by week, in arrays
from Player import Player

ROSTER_SIZE = 18


class Team:

    def __init__(self, index, dataset):
        # season variables like team name and index
        self.name = dataset.iloc[index, 0]
        self.index = index
        self.schedule = []
        # weekly variables, updated once after the game
        self.score = dataset.iloc[index, :]
        self.record = [0, 0, 0]
        self.adjusted_total_record = [0, 0, 0]
        self.roster = []
        self.weekly_standings = dataset
        # gametime variables, updated during the week for the game
        self.tpf = 0
        self.qb = None
        self.rb = []
        self.wr = []
        self.te = None
        self.flex = None
        self.dst = None
        self.k = None
        self.bench = []
        self.ir = []

    def set_schedule(self, schedule):
        self.schedule = schedule

    def update_roster(self, dataset):
        tmp = []
        # iterate through each character in the entire team roster excel sheet
        for i in range(len(dataset.index)):
            # check if on correct team
            if dataset.iloc[i, 2] == self.index:
                tmp.append(Player(dataset, i))
        for j in self.roster:
            cond = False  # variable assumes player isn't on lineup
            for k in tmp:
                if j.name == k.name:
                    cond = True
            # if player not on team, drop him
            if not cond:
                self.drop(j)
        for j in tmp:
            cond = False  # variable assumes player isn't on lineup
            for k in self.roster:
                if j.name == k.name:
                    cond = True
            # if player not on tmp, add him
            if not cond:
                self.add(j)

    def set_lineup(self, dataset):
        for i in range(len(dataset.index)):
            # finds if the team is on home side
            if dataset.iloc[i, 1] == self.index:
                if dataset.iloc[i, 9] == 'QB':
                    for player in self.roster:
                        if dataset.iloc[i, 3] == player.id or dataset.iloc[i, 5] == player.name:
                            self.qb = player
                elif dataset.iloc[i, 9] == 'RB':
                    for player in self.roster:
                        if dataset.iloc[i, 3] == player.id or dataset.iloc[i, 5] == player.name:
                            self.rb.append(player)
                elif dataset.iloc[i, 9] == 'WR':
                    for player in self.roster:
                        if dataset.iloc[i, 3] == player.id or dataset.iloc[i, 5] == player.name:
                            self.wr.append(player)
                elif dataset.iloc[i, 9] == 'TE':
                    for player in self.roster:
                        if dataset.iloc[i, 3] == player.id or dataset.iloc[i, 5] == player.name:
                            self.te = player
                elif dataset.iloc[i, 9] == 'Flex':
                    for player in self.roster:
                        if dataset.iloc[i, 3] == player.id or dataset.iloc[i, 5] == player.name:
                            self.flex = player
                elif dataset.iloc[i, 9] == 'K':
                    for player in self.roster:
                        if dataset.iloc[i, 3] == player.id or dataset.iloc[i, 5] == player.name:
                            self.k = player
                elif dataset.iloc[i, 9] == 'D/ST':
                    for player in self.roster:
                        if dataset.iloc[i, 3] == player.id or dataset.iloc[i, 5] == player.name:
                            self.dst = player
                elif dataset.iloc[i, 9] == 'IR':
                    for player in self.roster:
                        if dataset.iloc[i, 3] == player.id or dataset.iloc[i, 5] == player.name:
                            self.ir.append(player)
                elif dataset.iloc[i, 9] == 'Bench':
                    for player in self.roster:
                        if dataset.iloc[i, 3] == player.id or dataset.iloc[i, 5] == player.name:
                            self.bench.append(player)
            # finds if the team is on the away side
            elif dataset.iloc[i, 13] == self.index:
                if dataset.iloc[i, 21] == 'QB':
                    for player in self.roster:
                        if dataset.iloc[i, 15] == player.id or dataset.iloc[i, 17] == player.name:
                            self.qb = player
                elif dataset.iloc[i, 21] == 'RB':
                    for player in self.roster:
                        if dataset.iloc[i, 15] == player.id or dataset.iloc[i, 17] == player.name:
                            self.rb.append(player)
                elif dataset.iloc[i, 21] == 'WR':
                    for player in self.roster:
                        if dataset.iloc[i, 15] == player.id or dataset.iloc[i, 17] == player.name:
                            self.wr.append(player)
                elif dataset.iloc[i, 21] == 'TE':
                    for player in self.roster:
                        if dataset.iloc[i, 15] == player.id or dataset.iloc[i, 17] == player.name:
                            self.te = player
                elif dataset.iloc[i, 21] == 'Flex':
                    for player in self.roster:
                        if dataset.iloc[i, 15] == player.id or dataset.iloc[i, 17] == player.name:
                            self.flex = player
                elif dataset.iloc[i, 21] == 'K':
                    for player in self.roster:
                        if dataset.iloc[i, 15] == player.id or dataset.iloc[i, 17] == player.name:
                            self.k = player
                elif dataset.iloc[i, 21] == 'D/ST':
                    for player in self.roster:
                        if dataset.iloc[i, 15] == player.id or dataset.iloc[i, 17] == player.name:
                            self.dst = player
                elif dataset.iloc[i, 21] == 'IR':
                    for player in self.roster:
                        if dataset.iloc[i, 15] == player.id or dataset.iloc[i, 17] == player.name:
                            self.ir.append(player)
                elif dataset.iloc[i, 21] == 'Bench':
                    for player in self.roster:
                        if dataset.iloc[i, 15] == player.id or dataset.iloc[i, 17] == player.name:
                            self.bench.append(player)

    def optimize_lineup(self):
        # create temporary lineup list
        lineup = [self.qb, self.rb[0], self.rb[1], self.wr[0], self.wr[1], self.te, self.flex, self.dst, self.k]
        for tmp in self.bench:
            lineup.append(tmp)
        # reorder lineup list
        for player in range(len(lineup)):
            if lineup[player].position == 'RB' and lineup[player].points > lineup[1].points:
                lineup[player], lineup[1] = lineup[1], lineup[player]
            elif lineup[player].position == 'WR' and lineup[player].points > lineup[3].points:
                lineup[player], lineup[3] = lineup[3], lineup[player]
            elif lineup[player].position == 'TE' and lineup[player].points > lineup[5].points:
                lineup[player], lineup[5] = lineup[5], lineup[player]
        for player in range(len(lineup)):
            if player != 1 and lineup[player].position == 'RB' and lineup[player].points > lineup[2].points:
                lineup[player], lineup[2] = lineup[2], lineup[player]
            elif player != 3 and lineup[player].position == 'WR' and lineup[player].points > lineup[4].points:
                lineup[player], lineup[4] = lineup[4], lineup[player]
        for player in range(9, len(lineup)):
            if (lineup[player].position == 'WR' or lineup[player].position == 'RB' or lineup[
                    player].position == 'TE') and lineup[player].points > lineup[6].points:
                lineup[player], lineup[6] = lineup[6], lineup[player]
            elif lineup[player].position == 'QB' and lineup[player].points > lineup[0].points:
                lineup[player], lineup[0] = lineup[0], lineup[player]
            elif lineup[player].position == 'K' and lineup[player].points > lineup[8].points:
                lineup[player], lineup[8] = lineup[8], lineup[player]
            elif lineup[player].position == 'D/ST' and lineup[player].points > lineup[7].points:
                lineup[player], lineup[7] = lineup[7], lineup[player]
        # assign lineup to corresponding positions
        self.qb = lineup[0]
        self.rb[0] = lineup[1]
        self.rb[1] = lineup[2]
        self.wr[0] = lineup[3]
        self.wr[1] = lineup[4]
        self.te = lineup[5]
        self.flex = lineup[6]
        self.dst = lineup[7]
        self.k = lineup[8]

    def set_tpf(self):
        self.tpf = 0
        self.tpf += self.qb.points
        self.tpf += self.rb[0].points + self.rb[1].points
        self.tpf += self.wr[0].points + self.wr[1].points
        self.tpf += self.te.points
        self.tpf += self.flex.points
        self.tpf += self.dst.points
        self.tpf += self.k.points

    def get_roster(self):
        tmp = ''
        for j in self.roster:
            tmp += j.name + ' | '
        return tmp

    def get_lineup(self):
        tmp = ''
        tmp += 'Starting QB: ' + self.qb.name + '\n'
        tmp += 'Starting RBs: ' + self.rb[0].name + self.rb[1].name + '\n'
        tmp += 'Starting WRs: ' + self.wr[0].name + self.wr[1].name + '\n'
        tmp += 'Starting TE: ' + self.te.name + '\n'
        tmp += 'Starting Flex: ' + self.flex.name + '\n'
        tmp += 'Starting D/ST: ' + self.dst.name + '\n'
        tmp += 'Starting K: ' + self.k.name + '\n'
        return tmp

    def drop(self, player):
        self.roster.remove(player)

    def add(self, player):
        self.roster.append(player)


    # TODO dictionary to simplify code or classes
