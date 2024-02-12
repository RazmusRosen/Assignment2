import os
import random


class Dice:
    def __init__(self):
        self.diceValue = 1

    def getRandomDiceValue(self):
        return random.randint(1, 6)

    def getValue(self):
        return self.diceValue


class Player:
    def __init__(self):
        self.playerName = input("Enter your name: ")
        self.points = 0

    def getPlayerName(self):
        return self.playerName

    def tossDice(self, dice):
        value = dice.getRandomDiceValue()
        print(self.getPlayerName() + " got a " + str(value))
        return value

    def setPoints(self, value):
        self.points += value

    def getPoints(self):
        return self.points


class HighScore:
    def __init__(self):
        self.file = "HighScores.txt"
        self.createFile(self.file)

    def createFile(self, file):
        if os.path.exists(file):
            pass
        else:
            with open(file, "w") as file:
                file.write("High scores")

    def postHighScore(self, winner):
        winnersName = winner.getPlayerName()
        points = winner.getPoints()
        with open(self.file, "a") as file:
            file.write(winnersName + ":" + str(points)+"\n")
        highScoreDic = {}
        #pointsList = []
        with open(self.file, "r") as file:
            file.read
            for line in file:
                name, points = line.strip().split(":")
                if name in highScoreDic:
                    highScoreDic[name].append(points)
                else:
                    highScoreDic[name] = [points]
            print(highScoreDic)

    def whoWon(self, winner):
        self.postHighScore(winner)
        return winner.getPlayerName() + " won!"


class Game:
    def __init__(self):
        self.gameStatus = True

    def endGame(self):
        self.gameStatus = False

    def getGameStatus(self):
        return self.gameStatus

    def gameIsOn(self, dice, player):
        highscore = HighScore()
        totalPoints = player.getPoints()
        while (player.getPoints() < 100):
            playerPoints = player.tossDice(dice)
            if (playerPoints != 1):
                totalPoints += playerPoints
                print(player.getPlayerName() + " have " + str(totalPoints) + " point(s)")
                if (totalPoints < 100):
                    choice = input("Stay or toss: ")
                    choice = choice.lower()
                    if (choice == "toss"):
                        continue
                    else:
                        player.setPoints(totalPoints)
                        points = player.getPoints()
                        print(player.getPlayerName() + " got " + str(points) + " point(s)\n")
                        return False
                elif (totalPoints >= 100):
                    Game.endGame()
                    highscore.whoWon(player)
            elif (playerPoints == 1):
                print(player.getPlayerName() + " have " + str(player.getPoints()) + " point(s)\n")
                return False


def main():
    player1 = Player()
    player2 = Player()
    dice = Dice()
    HighScoreManager = HighScore()
    game = Game()
    while (game.gameStatus):
        player1Plays = True
        player2Plays = True
        while (player1Plays):
            player1Plays = game.gameIsOn(dice, player1)
        while (player2Plays):
            player2Plays = game.gameIsOn(dice, player2)
    

    """ player1Plays = True
    player2Plays = True
    player1Point = player1.getPoints()
    player2Point = player2.getPoints()

    while (player1Plays or player2Plays and player1Point < 100 or player2Point < 100):

        if (player1Plays is True):
            player1Points = player1.tossDice(dice)
            if (player1Points != 1):
                player1Point += player1Points
                print(player1.getPlayerName() + " have " + str(player1Point) + " point(s)")
                choice = input("Do you want to stay or toss? ")
                if (choice == "toss"):
                    continue
                else:
                    print("Okay " + player1.getPlayerName() + " stayed with " + str(player1Point) + " point(s)\n")
                    player1.setPoints(player1Point)
                    player1Plays = False
                    player2Plays = True
            elif (player1Points == 1):
                print(player1.getPlayerName() + " have " + str(player1.getPoints()) + " point(s)\n")
                player1Plays = False
                player2Plays = True

        elif (player2Plays is True and player1Plays is False):
            player2Points = player2.tossDice(dice)
            if (player2Points != 1):
                player2Point += player2Points
                print(player2.getPlayerName() + " have " + str(player2Point) + " point(s)")
                choice = input("Do you want to stay or toss? ")
                if (choice == "toss"):
                    continue
                else:
                    player2.setPoints(player2Point)
                    print("Player: " + player2.getPlayerName() + " got " + str(player2Point) + " point(s)\n")
                    player2Plays = False
                    player1Plays = True
            elif (player2Points == 1):
                print(player2.getPlayerName() + " have " + str(player2.getPoints()) + " point(s)\n")
                player2Plays = False
                player1Plays = True
 """
    result = HighScoreManager.whoWon(player1, player2)
    print(result)


if __name__ == '__main__':
    main()
