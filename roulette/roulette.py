import numpy as np

class Roulette:
    toText = {0 : "RED", 1 : "BLACK"}
    results = []

    def play(self):
            num = int(np.random.choice(3, 1, replace = True, p=[18/37, 18/37, 1/37])[0])
            self.results.append(num)
            return num

    def getResults(self):
        return self.results

    def getTextResults(self):
        return [self.toText[val] for val in self.results]
    
    def getStatistics(self, lastNumbers = 0):
        all = False
        black = 0
        if lastNumbers == 0 or lastNumbers >= len(self.results):
            all = True
        if all:
            for val in self.results:
                black += val
            return {"RED": round(1 - black/len(self.results), 3), "BLACK" : round(black/len(self.results), 3)}
        for val in self.results[-lastNumbers:]:
            black += val
        return {"RED": round(1 - black/lastNumbers, 3), "BLACK" : round(black/lastNumbers, 3)}
        

class Player():

    R1 = Roulette()
    turnover, maxStrike, maxLoss, investments, gameOver, strike = 0, 0, 0, 0, -1, 0
    toNum = {"RED" : 0,"BLACK" : 1}

    def __init__(self, investedCapital = 315, minBet = 5):
        self.minBet = minBet
        self.investedCapital = investedCapital
        self.moneyToPlay = investedCapital

    def play(self, roundsToPlay = 100, times = 2, lotPlayerAnalysis = False, strikeInRow = 5):
        # return of -1 is best case (no out of money), otherwise number indicates the round of failure
        roundResult, currLoss, currStrike, last = 0, 0, 0, 0
        currInvest = self.minBet
        if self.minBet > self.moneyToPlay:
            if not lotPlayerAnalysis:
                print("Out of Money!! You can't play anymore!")
            self.gameOver = 0
            return self.gameOver

        for r in range(roundsToPlay):
            roundResult = self.R1.play()
            if self.strike == 0 or last == roundResult:
                self.strike += 1

            if self.strike >= strikeInRow:
                self.turnover += currInvest
                if not roundResult == last:
                    self.investments += 1
                    self.moneyToPlay += currInvest
                    currInvest = self.minBet
                    currStrike += 1
                    if currLoss > self.maxLoss:
                        self.maxLoss = currLoss
                    currLoss= 0
                else:
                    self.moneyToPlay -= currInvest
                    currInvest *= times
                    currLoss += 1
                    if currStrike > self.maxStrike:
                        self.maxStrike = currStrike
                    currStrike = 0

                if currInvest > self.moneyToPlay:
                    self.gameOver = r + 1
                    return self.gameOver
            last = roundResult
        return -1
    
    def getResults(self):
        return {"moneyToPlay": self.moneyToPlay, "gameOver": self.gameOver, "maxStrike": self.maxStrike, "maxLoss": self.maxLoss, "turnover": self.turnover}


# For analysis
if __name__ == '__main__':
    # change these values, but not more in this file
    investedCapital, minBet, sIR, players, playRounds = 315, 5, 0, 1000, 1000
    P1 = Player(investedCapital, minBet)
    P1.play(roundsToPlay = playRounds, lotPlayerAnalysis = True, strikeInRow = sIR)
    print(P1.getResults())