import urllib.request
import requests
import lxml.html as lh
import pandas as pd

def get_lineups(year):
    mlb_teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHA', 'CHN', 'CIN', 'CLE', 'COL',
       'DET', 'FLO', 'HOU', 'KCA', 'LAA', 'LAN', 'MIL', 'MIN', 'NYA',
       'NYN', 'OAK', 'PHI', 'PIT', 'SDN', 'SEA', 'SFN', 'SLN', 'TBA',
       'TEX', 'TOR', 'WAS']
    teams = mlb_teams
    lineups = pd.DataFrame(data = {'team' : mlb_teams, 'players' : np.nan})

    for i in range(len(teams)):
        team = teams[i]
        query = str("SELECT playerID FROM Batting WHERE teamID = '" + team + "' AND yearID = " + year + " AND AB > 200")
        team_results = cur.execute(query).fetchall()
        flat_team = [item for sublist in team_results for item in sublist]
        flat_team = [item + "_" + year for item in flat_team]
        lineups.players[i] = flat_team[0:9]
    return lineups.players

def get_schedule(team, year):
    url = "https://www.baseball-reference.com/teams/" + team + "/" + year + "-schedule-scores.shtml#team_schedule"
    #Create a handle, page, to handle the contents of the website
    page = requests.get(url)
    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')
    tr_elements = doc.xpath('//tr')
    #Create empty list
    col=[]
    i=0
    #For each row, store each first element (header) and an empty list
    for t in tr_elements[0]:
        i+=1
        name=t.text_content()
        # print '%d:"%s"'%(i,name)
        col.append((name,[]))
    #Since out first row is the header, data is stored on the second row onwards
    for j in range(1,len(tr_elements)):
        #T is our j'th row
        T=tr_elements[j]

        #If row is not of size 10, the //tr data is not from our table 
        #if len(T)!=10:
        #    break

        #i is the index of our column
        i=0

        #Iterate through each element of the row
        for t in T.iterchildren():
            data=t.text_content() 
            #Check if row is empty
            if i>0:
            #Convert any numerical value to integers
                try:
                    data=int(data)
                except:
                    pass
            #Append the data to the empty list of the i'th column
            col[i][1].append(data)
            #Increment i for the next column
            i+=1
    Dict={title:column for (title,column) in col}
    bsched=pd.DataFrame(Dict)
    #bsched = pd.read_table('boston_schedule.txt', sep=",")
    bsched = bsched[['Tm', 'Opp', 'W/L']]
    bsched['W/L'][bsched['W/L'] == "W-wo"] = "W"
    bsched['W/L'][bsched['W/L'] == "L-wo"] = "L"
    pd.factorize(bsched["W/L"])
    bsched.Opp[bsched.Opp == "NYY"] = "NYA"
    bsched.Opp[bsched.Opp == "TBR"] = "TBA"
    bsched.Opp[bsched.Opp == "KCR"] = "KCA"
    bsched.Opp[bsched.Opp == "STL"] = "SLN"
    bsched.Opp[bsched.Opp == "CHW"] = "CHN"
    bsched = bsched[bsched.Tm != "Tm"]
    return bsched

# Examples
get_schedule("DET", "2014")
get_lineups("2010")
