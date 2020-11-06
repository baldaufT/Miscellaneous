import pickle
from roulette import Player

investedCapital, minBet, strikeInRowNeeded, players, playRounds = 315, 5, 5, 10000, 10000

P1 = [Player(investedCapital, minBet) for i in range(players)]
Results, moneyToPlay, gameOver, gameOverQuote, maxStrike, maxLoss, turnover, totalmaxLoss = [], 0, 0, 0, 0, 0, 0, 0

for p in P1:   # change maybe as well 'roundsToPlay' to your fav value
    p.play(roundsToPlay = playRounds, lotPlayerAnalysis = True, strikeInRow = strikeInRowNeeded)
    Results.append(p.getResults())

for r in Results:
    moneyToPlay += r["moneyToPlay"]
    maxStrike += r["maxStrike"]
    maxLoss += r["maxLoss"]
    if r["maxLoss"] > totalmaxLoss:
        totalmaxLoss = r["maxLoss"]
    turnover += r["turnover"]
    if r["gameOver"] >= 0:
        gameOverQuote += 1
        gameOver += r["gameOver"]

gameOver = gameOver / gameOverQuote
gameOverQuote = gameOverQuote / players
moneyToPlay = moneyToPlay / players
maxStrike = maxStrike / players
maxLoss = maxLoss / players
turnover = turnover / players

AvgResults = [moneyToPlay, maxStrike, maxLoss, turnover, gameOver, gameOverQuote]

print("\n\tTotal Loss Strike:\t", totalmaxLoss)
print("\n\tmoneyToPlay:\t\t", AvgResults[0],"\n\tmaxStrike:\t\t", AvgResults[1], "\n\tmaxLoss:\t\t", AvgResults[2], "\n\tturnover:\t\t", AvgResults[3], "\n\tgameOver:\t\t", str(round(AvgResults[4], 2)), "\n\tgameOverQuote:\t\t", str(round(AvgResults[5] * 100, 2)), "%\n")

with open("roulette_total_values.p", "wb") as file:
    pickle.dump(Results, file)

with open("roulette_avg_values.p", "wb") as f:
    pickle.dump(AvgResults, f)


