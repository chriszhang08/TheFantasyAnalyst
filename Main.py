import pandas as pd
import openpyxl

# import fantasy data sheet
from Team import Team
from Player import Player

scoreboard = pd.read_excel(r'D:\Documents\Computer Science\Incubator Project\league_data.xlsx')
op_scoreboard = pd.read_excel(r'D:\Documents\Computer Science\Incubator Project\optimized_league_data.xlsx')
# change this file with each date
box_score = pd.read_excel(r'D:\Documents\Computer Science\Incubator Project\box_score_sp1_mp1.xlsx')
players = pd.read_excel(r'D:\Documents\Computer Science\Incubator Project\team_roster_sp1_mp1.xlsx')
draft_recap = pd.read_excel(r'D:\Documents\Computer Science\Incubator Project\draft_recap2020.xlsx')

date = 2
LEAGUE_SIZE = 12
ROSTER_SIZE = 18

league_list = []
player_list = []
standings = []

# initialize each fantasy team object
for i in range(LEAGUE_SIZE):
    league_list.append(Team(i, scoreboard))

# manually initialize schedule
league_list[5].set_schedule([10, 0, 6, 1, 3, 11, 8, 4, 7, 2, 9, 10, 0, 11, 11, 1, 1])
league_list[7].set_schedule([9, 10, 0, 6, 1, 3, 11, 8, 5, 4, 2, 9, 10, 9, 9, 3, 3])
league_list[2].set_schedule([4, 9, 10, 0, 6, 1, 3, 11, 8, 5, 7, 4, 9, 4, 4, 6, 6])
league_list[9].set_schedule([7, 2, 4, 10, 0, 6, 1, 3, 11, 8, 5, 7, 2, 7, 7, 0, 0])
league_list[10].set_schedule([5, 7, 2, 9, 4, 0, 6, 1, 3, 11, 8, 5, 7, 1, 1, 11, 11])
league_list[0].set_schedule([8, 5, 7, 2, 9, 10, 4, 6, 1, 3, 11, 8, 5, 8, 8, 9, 9])
league_list[6].set_schedule([11, 8, 5, 7, 2, 9, 10, 0, 4, 1, 3, 11, 8, 3, 3, 2, 2])
league_list[1].set_schedule([3, 11, 8, 5, 7, 2, 9, 10, 0, 6, 4, 3, 11, 10, 10, 5, 5])
league_list[3].set_schedule([1, 4, 11, 8, 5, 7, 2, 9, 10, 0, 6, 1, 4, 6, 6, 7, 7])
league_list[11].set_schedule([6, 1, 3, 4, 8, 5, 7, 2, 9, 10, 0, 6, 1, 5, 5, 10, 10])
league_list[8].set_schedule([0, 6, 1, 3, 11, 4, 5, 7, 2, 9, 10, 0, 6, 0, 0, 4, 4])
league_list[4].set_schedule([2, 3, 9, 11, 10, 8, 0, 5, 6, 7, 1, 2, 3, 2, 2, 8, 8])


def draft_roster():
    for i in range(len(draft_recap.index)):
        league_list[draft_recap.iloc[i, 4]].roster.append(Player(draft_recap, i))


def calculate_record(team):
    for i in range(1, date + 1):
        if league_list[find_opponent(team, i)].score[i] < league_list[team].score[i]:
            league_list[team].record[0] += 1
        elif league_list[find_opponent(team, i)].score[i] > league_list[team].score[i]:
            league_list[team].record[1] += 1
        else:
            league_list[team].record[2] += 1

    return league_list[team].record


# calculate adjusted record (each team plays every opposing team each week)
def adjusted_record(team):
    # initialize record array
    for week in range(1, date + 1):
        my_team_score = league_list[team].score[week]
        for i in range(LEAGUE_SIZE):
            their_team_score = league_list[i].score[week]
            if team != i:
                if my_team_score > their_team_score:
                    league_list[team].adjusted_total_record[0] += 1
                elif my_team_score < their_team_score:
                    league_list[team].adjusted_total_record[1] += 1
                else:
                    league_list[team].adjusted_total_record[2] += 1

    return league_list[team].adjusted_total_record


# calculate the direct head to head record between two teams
def adjusted_h2h_record(team1, team2):
    record = [0, 0, 0]
    for week in range(1, date + 1):
        if league_list[team1].score[week] > league_list[team2].score[week]:
            record[0] += 1
        if league_list[team1].score[week] < league_list[team2].score[week]:
            record[1] += 1
        if league_list[team1].score[week] == league_list[team2].score[week]:
            record[2] += 1
    return record


# convert array into readable record format
def print_adjusted_record():
    for index in range(LEAGUE_SIZE):
        print(str(league_list[index].name) + str(league_list[index].adjusted_total_record[0]) + '-' +
              str(league_list[index].adjusted_total_record[1]) + '-' + str(league_list[index].adjusted_total_record[2]))


# find the opponent of the nth team on a certain week
def find_opponent(index, week):
    return league_list[index].schedule[week - 1]


# find average margin of victory, and smallest average margin of victory
def margin_of_victory(index, week):
    opponent_score = scoreboard.iloc[find_opponent(index, week), week]
    team_score = scoreboard.iloc[index, week]
    return team_score - opponent_score


# returns the average margin of victory for a given week
def avg_margin_of_victory(week):
    accumulator = 0
    for team in range(LEAGUE_SIZE):
        if margin_of_victory(team, week) >= 0:
            accumulator += margin_of_victory(team, week)
    return accumulator / (LEAGUE_SIZE / 2)


# return the average score of a given week
def avg_points_scored(week):
    accumulator = 0
    for team in range(LEAGUE_SIZE):
        accumulator += league_list[team].tpf
    return accumulator / LEAGUE_SIZE


# return the median score of a given week
def med_points_scored(week):
    ordered = scoreboard.iloc[:, week].tolist()[:-1]
    # Traverse through all array elements
    for i in range(LEAGUE_SIZE):
        # Last i elements are already in place
        for j in range(0, LEAGUE_SIZE - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if ordered[j] > ordered[j + 1]:
                ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]
    return (ordered[int(LEAGUE_SIZE / 2 - 1)] + ordered[int(LEAGUE_SIZE / 2)]) / 2


# calculate league standings
def league_standings(week):
    for i in range(LEAGUE_SIZE):
        standings.append(league_list[i])
    for j in range(LEAGUE_SIZE):
        # Last i elements are already in place
        for k in range(0, LEAGUE_SIZE - j - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if standings[k].record[0] < standings[k + 1].record[0]:
                standings[k], standings[k + 1] = standings[k + 1], standings[k]
            elif standings[k].record[0] == standings[k + 1].record[0]:
                if standings[k].tpf < standings[k + 1].tpf:
                    standings[k], standings[k + 1] = standings[k + 1], standings[k]
    return standings


# calculate certain attributes of teams
# initialize my roster

draft_roster()

# seasonal/weekly update loop
for i in range(LEAGUE_SIZE):
    adjusted_record(i)
    calculate_record(i)
    league_list[i].update_roster(players)
    print(league_list[i].name + str(league_list[i].record))
    # print(league_list[0].get_roster())

print_adjusted_record()

# daily update loop
for i in range(LEAGUE_SIZE):
    league_list[i].set_lineup(box_score)
    for j in range(len(league_list[i].roster)):
        league_list[i].roster[j].set_player_performance(box_score, i)
        # print(league_list[i].roster[j].name + str(league_list[i].roster[j].points))
    league_list[i].set_tpf()
    league_list[i].optimize_lineup()
    league_list[i].set_tpf()

# after optimized lineup
for i in range(LEAGUE_SIZE):
    adjusted_record(i)
    calculate_record(i)
    op_scoreboard.iloc[i, date] = league_list[i].tpf
    print(league_list[i].name + str(league_list[i].record))

    # print(league_list[0].get_roster())

print_adjusted_record()
# print(league_list[find_opponent(0, date)].name)
# print(league_list[10].record)
# print(avg_margin_of_victory(date))


# test writing own excel sheet
writer = pd.ExcelWriter('test1.xlsx', engine='xlsxwriter')
op_scoreboard.to_excel(writer, sheet_name='Sheet1')
writer.save()

'''
for i in range(LEAGUE_SIZE):
    print(league_standings(date)[i].name + str(league_standings(date)[i].record) + ' ' +
          str(league_standings(date)[i].tpf))
'''
'''
for week in range(1, date + 1):
    for team in range(12):
        print(box_score.iloc[team, 0] + 'margin of victory of week ' + str(week) + ' is ' + str(margin_of_victory(team, week)))
    print('average margin of victory for week ' + str(week) + ' is ' + str(avg_margin_of_victory(week)))
'''

# TODO find a way to look at standings
# TODO find a way to see how many points are scored at each position and bench and waivers
# TODO find a way to see the associated team each player is on
# TODO find a way to substitute players in each position
# TODO find a way to track transactions
# TODO find a way to incorporate draft position and player history (including projections)
# TODO find a way to get injury status
# TODO maybe something with waivers (budget/order)?
# TODO best possible draft pick within 10 picks
# TODO touchdowns vs yards per team
