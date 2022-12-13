from sklearn.metrics import confusion_matrix

def simulate_season(team, year):
    player_registry = PlayerRegistry()
    player_registry.load_from_lahman()
    schedule = get_schedule(team, year)
    schedule.reset_index(drop=True, inplace=True)
    lineups = get_lineups(year)
    rotation = get_rotation(year)
    outcomes = np.empty(schedule.shape[0], dtype='object')
    #print(schedule)
    for i in range(schedule.shape[0]):  
        #print(i)
        team = schedule.Tm[i]
        opp = schedule.Opp[i]
        #print(team)
        #print(opp)
        
        team_lineup = lineups.players[lineups.team == team]
        team_lineup = team_lineup.to_list()[0]
        
        team_pitchers = rotation.players[rotation.team == team]
        team_pitchers = team_pitchers.to_list()[0]
        
        # print(opp)
        opp_lineup = lineups.players[lineups.team == opp]
        opp_lineup = opp_lineup.to_list()[0]
        
        opp_pitchers = rotation.players[rotation.team == opp]
        opp_pitchers = opp_pitchers.to_list()[0]
        
        while outcomes[i] == None:
            
            lineup = initialize_lineup()
            for j in range(9):
                # print(i)
                batter = team_lineup[j]
                try:
                    batter_object = player_registry.registry[batter]
                    lineup = update_lineup(lineup, j, batter_object)
                except:
                    pass
            team_outcome = return_mean_runs(batters = team_lineup, starter = team_pitchers[0:1], relievers = team_pitchers[1:4], starter_innings = 6)
            
            lineup = initialize_lineup()
            #print(opp_lineup)
            for j in range(9):
                # print(i)
                batter = opp_lineup[j]
                try:
                    batter_object = player_registry.registry[batter]
                    lineup = update_lineup(lineup, j, batter_object)
                except:
                    pass
            opp_outcome = return_mean_runs(batters = opp_lineup, starter = opp_pitchers[0:1], relievers = opp_pitchers[1:4], starter_innings = 6)
            
            if (team_outcome > opp_outcome):
                outcomes[i] = "W"
            elif (team_outcome < opp_outcome):
                outcomes[i] = "L"
        if i % 10 == 0:
            print("Sample simulated outcome: " + str(team) + ": " + str(team_outcome) + " vs. " + str(opp) + ": " + str(opp_outcome))
    print(outcomes)
    print(confusion_matrix(y_true = schedule["W/L"], y_pred = outcomes))
