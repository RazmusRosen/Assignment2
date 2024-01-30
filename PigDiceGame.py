import os
import random


class Dice:
    def __init__(self):
        self.diceValue = 1

    def getDiceValue(self):
        self.diceValue = random.randint(1, 6)
        return self.diceValue

    def getValue(self):
        return self.diceValue


class Player:
    def __init__(self):
        self.playerName = input("Enter your name: ")
        self.points = 0

    def getPlayerName(self):
        return self.playerName

    def tossDice(self, dice):
        value = dice.getDiceValue()
        print(self.getPlayerName() + " got a " + str(value))
        if value != 1:
            self.setPoints(value)
            return self.points
        else:
            value = 0
            self.setPoints(value)
            return self.points

    def setPoints(self, value):
        if value != 0:
            self.points += value
        else:
            self.points = value

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
    
    def postHighScore(self, player1Points, player2Points):
        highestScore = player1Points
        if (player2Points > highestScore):
            pass


def main():
    player1 = Player()
    player2 = Player()
    dice = Dice()
    HighScore()

    player1Plays = True
    player2Plays = True
    
    while (player1Plays):
        player1Points = player1.tossDice(dice)
        print("Player: " + player1.getPlayerName() + " got " + str(player1Points) + " point(s)")
        if (player1Points != 0):
            choice = input("Do you want to stay or toss? ")
            if (choice == "toss"):
                continue
            else:
                print("Okay you stayed with " + str(player1Points) + " point(s)")
                player1Plays = False
        else:
            player1Plays = False
            player2Points = player2.tossDice(dice)
            print("Player: " + player2.getPlayerName() + " got " + str(player2Points) + " point(s)")
            if (player2Points == 0):
                print("It's a tie")
                player2Plays = False

    while (player2Plays):
        player2Points = dice.getValue
        if (player1Points == 0):
            print(player2.getPlayerName() + " you won!")
            player2Plays = False
        elif (player2Points != 0):
            player2Points = player2.tossDice(dice)
            print("Player: " + player2.getPlayerName() + " got " + str(player2Points) + " point(s)")

            choice = input("Do you want to stay or toss? ")
            if (choice == "toss"):
                continue
            else:
                player2Plays = False


if __name__ == '__main__':
    main()
