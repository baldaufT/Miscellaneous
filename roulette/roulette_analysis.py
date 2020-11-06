import pickle
from roulette import Player

investedCapital, minBet, strikeInRow, players, playRounds = 315, 5, 5, 1000, 1000

P1 = [Player(investedCapital, minBet, strikeInRow) for i in range(players)]
Results, AvgResults = [], []
moneyToPlay, gameOver, gameOverQuote, maxStrike, maxLoss, turnover = 0, 0, 0, 0, 0, 0

for p in P1:   # change maybe as well 'roundsToPlay' to your fav value
    p.play(roundsToPlay = playRounds, lotPlayerAnalysis = True)
    Results.append(p.getResults())

for r in Results:
    moneyToPlay += r["moneyToPlay"]
    maxStrike += r["maxStrike"]
    maxLoss += r["maxLoss"]
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

AvgResults.append(moneyToPlay)
AvgResults.append(maxStrike)
AvgResults.append(maxLoss)
AvgResults.append(turnover)
AvgResults.append(gameOver)
AvgResults.append(gameOverQuote)

print("\tmoneyToPlay:\t\t", AvgResults[0],"\n\tmaxStrike:\t\t", AvgResults[1], "\n\tmaxLoss:\t\t", AvgResults[2], "\n\tturnover:\t\t", AvgResults[3], "\n\tgameOver:\t\t", str(round(AvgResults[4], 2)), "\n\tgameOverQuote:\t\t", str(AvgResults[5] * 100), "%")

with open("roulette_total_values.p", "wb") as file:
    pickle.dump(Results, file)

with open("roulette_avg_values.p", "wb") as f:
    pickle.dump(AvgResults, f)


