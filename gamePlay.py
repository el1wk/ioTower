from tkinter import *
from ioObjects import *
from playerObjects import *

#game play rules

def moreHealthP1(data):
    x = data.playerOne.getLocation()[0]
    y = data.playerOne.getLocation()[1]
    x1 = data.playerOne.getLocation()[2]
    y1 = data.playerOne.getLocation()[3]
    for healthy in data.healths:
        if healthy.isCollision(x, y):
            return True
        elif healthy.isCollision(x1, y1):
            return True
    return False

def moreHealthP2(data):
    x = data.playerTwo.getLocation()[0]
    y = data.playerTwo.getLocation()[1]
    x1 = data.playerTwo.getLocation()[2]
    y1 = data.playerTwo.getLocation()[3]
    for healthy in data.healths:
        if healthy.isCollision(x, y):
            return True
        elif healthy.isCollision(x1, y1):
            return True
    return False

def canFlipP2(data):
    x = data.playerTwo.getLocation()[0]
    y = data.playerTwo.getLocation()[1]
    x1 = data.playerTwo.getLocation()[2]
    y1 = data.playerTwo.getLocation()[3]
    for flipy in data.flips:
        if flipy.isCollision(x, y):
            return True
        elif flipy.isCollision(x1, y1):
            return True

def canFlipP1(data):
    x = data.playerOne.getLocation()[0]
    y = data.playerOne.getLocation()[1]
    x1 = data.playerOne.getLocation()[2]
    y1 = data.playerOne.getLocation()[3]
    for flipy in data.flips:
        if flipy.isCollision(x, y):
            return True
        elif flipy.isCollision(x1, y1):
            return True

def morePointsP1(data):
    x = data.playerOne.getLocation()[0]
    y = data.playerOne.getLocation()[1]
    x1 = data.playerOne.getLocation()[2]
    y1 = data.playerOne.getLocation()[3]
    color = random.choice([data.playerOneTrailColor, data.playerTwoTrailColor])
    if data.theGoal.isCollision(x, y) or data.theGoal.isCollision(x1, y1):
        data.playerOnes.clear()
        data.playerTwos.clear()
        data.playerOne = player(data.sideMargin-10, data.topMargin,
        data.playerOneColor, 10, (1, 0))
        data.playerTwo = player(data.width-data.sideMargin, data.topMargin,
        data.playerTwoColor, 10, (-1, 0))
        if data.theGoal.getColor() == data.playerOneTrailColor:
            data.scoreValueP1 += 25
            data.playerOne.increaseSpeed()
            data.theGoal.changeColor(color)
        else:
            data.scoreValueP1 -= 25

def morePointsP2(data):
    x = data.playerTwo.getLocation()[0]
    y = data.playerTwo.getLocation()[1]
    x1 = data.playerTwo.getLocation()[2]
    y1 = data.playerTwo.getLocation()[3]
    color = random.choice([data.playerOneTrailColor, data.playerTwoTrailColor])
    if data.theGoal.isCollision(x, y) or data.theGoal.isCollision(x1, y1):
        data.playerOnes.clear()
        data.playerTwos.clear()
        data.playerOne = player(data.sideMargin-10, data.topMargin,
        data.playerOneColor, 10, (1, 0))
        data.playerTwo = player(data.width-data.sideMargin, data.topMargin,
        data.playerTwoColor, 10, (-1, 0))
        if data.theGoal.getColor() == data.playerTwoTrailColor:
            data.scoreValueP2 += 25
            data.playerTwo.increaseSpeed()
            data.theGoal.changeColor(color)
        else:
            data.scoreValueP2 -= 25

def canSwitch(data):
    #playerOne
    x = data.playerOne.getLocation()[0]
    y = data.playerOne.getLocation()[1]
    x1 = data.playerOne.getLocation()[2]
    y1 = data.playerOne.getLocation()[3]
    if (data.theSwitchZone.isCollision(x, y) or data.theSwitchZone.isCollision(x1, y1)):
        data.switch = True

    #playerTwo
    x2 = data.playerTwo.getLocation()[0]
    y2 = data.playerTwo.getLocation()[1]
    x12 = data.playerTwo.getLocation()[2]
    y12 = data.playerTwo.getLocation()[3]

    if (data.theSwitchZone.isCollision(x2, y2) or data.theSwitchZone.isCollision(x12, y12)):
        data.switch = True

def crash(data):
    clear =  False
    resetP1 = False
    resetP2 = False

    #player one crashing into player 2's trail
    x = data.playerOne.getLocation()[0]
    y = data.playerOne.getLocation()[1]
    x1 = data.playerOne.getLocation()[2]
    y1 = data.playerOne.getLocation()[3]
    for walls in data.playerTwos:
        if walls.isCollision(x, y) or walls.isCollision(x1, y1):
            data.reducePlayerOneHealth = True
            clear = True
            resetP1 = True

    #player two crashing into player 1's trail
    x2 = data.playerTwo.getLocation()[0]
    y2 = data.playerTwo.getLocation()[1]
    x12 = data.playerTwo.getLocation()[2]
    y12 = data.playerTwo.getLocation()[3]
    for walls in data.playerOnes:
        if walls.isCollision(x2, y2) or walls.isCollision(x12, y12):
            data.reducePlayerTwoHealth = True
            clear = True
            resetP2 = True

    if resetP1:
        data.playerOne = player(data.sideMargin-10, data.topMargin,
        data.playerOneColor, 10, (1, 0))
        resetP1 = False

    if resetP2:
        data.playerTwo = player(data.width-data.sideMargin, data.topMargin,
        data.playerTwoColor, 10, (-1, 0))
        resetP2 = False

    if clear:
        data.playerOnes.clear()
        data.playerTwos.clear()
        clear = False
