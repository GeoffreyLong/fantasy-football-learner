#TODO
#   Get the defensive players
#       Right now I might only be getting offensive... I will have to check
#   Add nfldb 
#       Implementation: https://github.com/BurntSushi/nfldb
#       Actual DB (most recent): http://burntsushi.net/stuff/nfldb/nfldb.sql.zip
#       This might make it easier to aggregate the information
#       It will also make it faster


import nflgame

class DataPoint:
    # NOTE Could add
    #   Home vs away
    #   Position
    def __init__(self):
        self.ownTeam = None
        self.oppTeam = None
        self.output = None
        self.playerIdx = None

class AttemptOne:
    def setPlayerDict(self):
        # TEMP reducion for testing
        #total = []
        #for year in range(2009, 2016):
        #    season = nflgame.games(year)
        #    total = total + season
        total = nflgame.games(2015);

        players = nflgame.combine_game_stats(total)
        curId = 0
        for p in players:
            if (not self.playerDict.get(p.playerid)):
                self.playerDict[p.playerid] = curId
                curId += 1

        self.playerCount = curId
        # Outputs 3694


    def runDataAcq(self):
        # TEMP reducion for testing
        # for year in range(2009, 2016):
        #    season = nflgame.games(year)
        season = nflgame.games(2015);
        for game in season:
            game = [game]
            players = nflgame.combine_game_stats(game)

            # Get a list of players that are on each team
            homeTeam = [];
            awayTeam = [];
            for p in players.filter(home=True):
                homeTeam.append(self.playerDict.get(p.playerid))
            for p in players.filter(home=False):
                awayTeam.append(self.playerDict.get(p.playerid))
                

            for p in players.limit(10): 
                dataPt = DataPoint()
                dataPt.playerIdx = self.playerDict.get(p.playerid)
                dataPt.output = self.formatOutput(p.stats)

                if (p.home):
                    dataPt.ownTeam = homeTeam
                    dataPt.oppTeam = awayTeam
                else:
                    dataPt.ownTeam = awayTeam
                    dataPt.oppTeam = homeTeam

                self.dataPoints.append(dataPt)
            # for p in players.rushing().sort("rushing_yds").limit(10):
            #    print p
            #for p in players.sort('id'):
                #print p, p.playerid
        
    def formatOutput(self, p):
        # [passAtt, passCmp, passYds, passTDs, passTwoPt, interceptions,
        #   receptions, receivingYds, receivingTDs, receivingTwoPt,
        #   rushingAtt, rushingYds, rushingTDs, rushingTwoPt, fumbles,
        #   puntret_tds, kickret_tds]
        # 
        # NO RECEIVING TARGETS???
        # FOR LATER: 
        #   points (fantasy) if I can get them from online
        #   long attempts for each if helpful


        # Is there a cleaner, more pythonic, way to do this? 
        out = [0] * 16
        out[0] = p.get('passing_att', 0);
        out[1] = p.get('passing_cmp', 0);
        out[2] = p.get('passing_yds', 0);
        out[3] = p.get('passing_tds', 0);
        out[4] = p.get('passing_twoptm', 0);
        out[5] = p.get('passing_ints', 0);
        out[6] = p.get('receiving_rec', 0);
        out[7] = p.get('receiving_yds', 0);
        out[8] = p.get('receiving_tds', 0);
        out[9] = p.get('receiving_twoptm', 0);
        out[10] = p.get('rushing_att', 0);
        out[11] = p.get('rushing_yds', 0);
        out[12] = p.get('rushing_tds', 0);
        out[13] = p.get('rushing_twoptm', 0);
        out[14] = p.get('puntret_tds', 0);
        out[15] = p.get('kickret_tds', 0);

        # print out
        return out


    def __init__(self):
        self.playerDict = {}
        self.dataPoints = []
        self.setPlayerDict()



# class DataPoint:
    # Will be an input and an output


# class input:
    # Will be the players of the game
    # So this initial attempt will be rather large and cumbersome
    # It will essentially be a combination of two super sparse vectors
    #   The first is a vector of 0's where the player whose metrics we want is 1
    #   The second is a vector where active teammates are 1's, opponents are -1's
    # Each input will be 7388 in length with only about 100 of these non-zeroed
    # I will attempt at a smarter implementation when I try this out

def main():
    att = AttemptOne()
    att.runDataAcq();

    for dataPt in att.dataPoints:
        print dataPt.ownTeam




def aggregateData():
    return None

if __name__ == "__main__":
    main()
