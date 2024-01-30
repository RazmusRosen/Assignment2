import random


class Dice:
    def __init__(self):
        self.diceValue = random.randint(1, 6)

    def tossDice(self):
        self.diceValue = random.randint(1, 6)
        return self.diceValue


class Player:
    def __init__(self):
        self.playerName = input("Enter your name: ")

    def getPlayerName(self):
        return self.playerName
    

def main():
    