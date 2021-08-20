from flask import Flask, request, jsonify, json

import Main

app = Flask(__name__)


@app.route('/')
def index():
    return {
        'names': [
            {'first': "Josh"},
            {'first': "Jacob"}
        ]
    }  # render_template('index.html')


@app.route('/analyze/', methods=['POST'])
def analyze():
    # create home and away team variables
    homeTeam = None
    awayTeam = None
    matchup = [request.json['homeName'], request.json['awayName']]
    for i in range(Main.LEAGUE_SIZE):
        if matchup[0] == Main.league_list[i].name:
            homeTeam = Main.league_list[i]
        elif matchup[1] == Main.league_list[i].name:
            awayTeam = Main.league_list[i]

    # optimize lineup of home team based on data from post request
    homeScore = request.json['homeScore']
    print(homeScore)
    for player in homeTeam.roster:
        for i in homeScore:
            if player.lineup == i:
                # overwrite existing points attribute in player object
                player.points = float(homeScore[i])
    for player in homeTeam.roster:
        print(player.name + str(player.lineup) + " | " + str(player.points))
    homeTeam.optimize_lineup()

    # optimize lineup of away team based on data from post request
    awayScore = request.json['awayScore']
    for player in awayTeam.roster:
        for i in awayScore:
            if player.lineup == i:
                # overwrite existing points attribute in player object
                player.points = float(awayScore[i])
    for player in awayTeam.roster:
        print(player.name + str(player.lineup) + " | " + str(player.points))
    awayTeam.optimize_lineup()

    hLineup = ["Starting QB: " + homeTeam.qb.name, "Starting RB1: " + homeTeam.rb[0].name, "Starting RB2: " + homeTeam.rb[1].name, "Starting WR1: " + homeTeam.wr[0].name, "Starting WR2: " + homeTeam.wr[1].name, "Starting TE: " + homeTeam.te.name, "Starting Flex: " + homeTeam.flex.name, "Starting DST: " + homeTeam.dst.name, "Starting K: " + homeTeam.k.name]
    for tmp in homeTeam.bench:
        hLineup.append("Bench: " + tmp.name)
    aLineup = ["Starting QB: " + awayTeam.qb.name, "Starting RB1: " + awayTeam.rb[0].name, "Starting RB2: " + awayTeam.rb[1].name, "Starting WR1: " + awayTeam.wr[0].name, "Starting WR2: " + awayTeam.wr[1].name, "Starting TE: " + awayTeam.te.name, "Starting Flex: " + awayTeam.flex.name, "Starting DST: " + awayTeam.dst.name, "Starting K: " + awayTeam.k.name]
    for tmp in awayTeam.bench:
        aLineup.append("Bench: " + tmp.name)
    pointsFor = awayTeam.score[0]
    optPointsFor = awayTeam.tpf
    margin = optPointsFor - pointsFor
    adjusted_h2h = Main.adjusted_h2h_record(1, 3)
    adjusted_record = Main.league_list[0].adjusted_total_record
    adjusted_opt_record = Main.league_list[0].adjusted_opt_record
    avg_points = Main.avg_points_scored(1)
    med_points = Main.med_points_scored(1)
    best_coach = Main.best_coach(1).name
    worst_coach = Main.worst_coach(1).name
    results = {
        'results': [
            #TODO fix this line so it can be JSON compatible
            {'lineup': aLineup},
            {'pointsFor': pointsFor},
            {'optPointsFor': optPointsFor},
            {'marginOfOpt': margin},
            {'adjRecord': adjusted_record},
            {'adjOptRecord': adjusted_opt_record},
            {'adjh2hRecord': adjusted_h2h},
            {'avgPointsPWeek': avg_points},
            {'bestCoach': best_coach},
            {'worstCoach': worst_coach},
            {'medPointsPWeek': med_points},
        ]
    }
    print("results")
    print(results)
    return results


if __name__ == '__main__':
    app.run(port=3000)
