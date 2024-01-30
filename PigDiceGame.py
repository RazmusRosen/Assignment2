import random


class Dice:
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
        print("You got a " + str(value))
        if value != 1:
            self.setPoints(value)
            return self.points
        else:
            return 1

    def setPoints(self, value):
        self.points += value

    def getPoints(self):
        return self.points


def main():
    player1 = Player()
    player2 = Player()
    dice = Dice()

    playing = True
    while (playing):
        player1Points = player1.tossDice(dice)
        player2Points = player2.tossDice(dice)

        print("Player: " + player1.getPlayerName() + " got " + str(player1Points) + " points")
        print("Player: " + player2.getPlayerName() + " got " + str(player2Points) + " points")

        if (player1Points == 1):
            print(player1.getPlayerName() + " lost")
            playing = False
        elif (player2Points == 1):
            print(player2.getPlayerName() + " lost")
            playing = False

        if playing is True:
            choice = input("Do you want to continue? ")
            if choice == "no":
                playing = False
        else:
            continue


if __name__ == '__main__':
    main()
