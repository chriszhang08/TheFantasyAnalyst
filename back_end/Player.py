import pandas as pd


class Player:
    def __init__(self, dataset, index):
        if dataset.columns[0] == 'Pick':
            self.id = -1
            self.name = dataset.iloc[index, 1]
            self.team = dataset.iloc[index, 3]
            self.position = dataset.iloc[index, 2]
            self.pick = dataset.iloc[index, 0]
            self.lineup = None
            self.points = 0
        else:
            self.id = dataset.iloc[index, 6]
            self.name = dataset.iloc[index, 8]
            self.team = dataset.iloc[index, 10]
            self.position = dataset.iloc[index, 11]
            self.pick = None
            self.lineup = None
            self.points = 0

    #                      boxscore dataset | home or away boolean value | team index
    def set_player_performance(self, dataset, index):
        # iterate through the box score dataset to set each players points scored
        for i in range(len(dataset.index)):
            # finds if the team is on home side
            if dataset.iloc[i, 1] == index:
                if dataset.iloc[i, 3] == self.id or dataset.iloc[i, 5] == self.name:
                    self.points = dataset.iloc[i, 10]
            # finds if the team is on the away side
            elif dataset.iloc[i, 13] == index:
                if dataset.iloc[i, 15] == self.id or dataset.iloc[i, 17] == self.name:
                    self.points = dataset.iloc[i, 22]

    def import_player_performance(self, points):
        self.points = points