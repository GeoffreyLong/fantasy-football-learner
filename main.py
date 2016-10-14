#TODO
#   Add nfldb


import nflgame

class AttemptOne:
    playerDict = {}
    playerCount = 0


    def setPlayerDict(self):
        total = []
        for year in range(2009, 2016):
            season = nflgame.games(year)
            total = total + season

        players = nflgame.combine_game_stats(total)
        curId = 0
        for p in players:
            if (not self.playerDict.get(p.playerid)):
                self.playerDict[p.playerid] = curId
                curId += 1

        self.playerCount = curId
        # Outputs 3694


    def runDataAcq():
        # TEMPORARILY REDUCE THE NUMBERS SO IT RUNS FASTER
        # for year in range(2009, 2016):
        #    season = nflgame.games(year)
        for week in range(1,15):
            season = nflgame.games(2013, week=week);
            for game in season:
                game = [game]
                players = nflgame.combine_game_stats(game)
                
                # Would be best to calculate the number of players dynamically
                playerArray = [0] * 3694;
                for p in players.filter(home=True):
                    if (not playerDict.get(p.playerid)):
                        playerDict[p.playerid] = curId
                        curId += 1
                    playerArray[curId] = 1

                print playerArray



                print 
                print
                #for p in players.rushing().sort("rushing_yds").limit(10):
                #    print p
                #for p in players.sort('id'):
                    #print p, p.playerid
        
    
    def __init__(self):
        # Ensures that this dict is only set up once
        if (not self.playerDict):   
            print "setting"
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




def aggregateData():
    return None

if __name__ == "__main__":
    main()
