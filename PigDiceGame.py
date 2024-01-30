import os
import random


class Dice:
    def __init__(self):
        self.diceValue = 1

    def getDiceValue(self):
        self.diceValue = random.randint(1, 6)
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


def main():
    player1 = Player()
    player2 = Player()
    dice = Dice()
    HighScore()

    playing = True
    while (playing):
        player1Points = player1.tossDice(dice)
        print("Player: " + player1.getPlayerName() + " got " + str(player1Points) + " point(s)")
        if (player1Points == 0):
            print(player1.getPlayerName() + " lost")
            break
        
        player2Points = player2.tossDice(dice)
        print("Player: " + player2.getPlayerName() + " got " + str(player2Points) + " point(s)")
        if (player2Points == 0):
            print(player2.getPlayerName() + " lost")
            break
            
        if playing is True:
            choice = input("Do you want to continue? ")
            if choice == "no":
                playing = False
printafasddadsada

if __name__ == '__main__':
    main()
