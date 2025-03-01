from tkinter import *
from ioObjects import *
from playerObjects import *
from gamePlay import*
import random
import math

#automates player that is not current player
#changes direction of player by calculating the shortest distance between it's
#current location, next move location, and the target
#the target changes depending on the goal color, and health
#if the health of the player is low, target will be health
#if the goal color matches player color, target will be goal
#if the goal color does not match player color, target will be switch

def automatedDirection(data):
    d = bestDistance(data)
    if data.currentPlayer == 0:
        data.playerTwo.changeDirection((d))
    else: data.playerOne.changeDirection((d))

    automatedToGoal(data)

def automatedToGoal(data):
    if data.currentPlayer == 0:
        if data.playerTwoHealth < 2:
            data.needsHealth = True
        else: data.needsHealth = False

        if data.theGoal.getColor() == data.playerTwo.getColor():
            data.getGoal = True
            data.needsSwitch = False
        else:
            data.getGoal = False
            data.needsSwitch = True

    if data.currentPlayer == 1:
        if data.playerOneHealth < 2:
            data.needsHealth = True
        else: data.needsHealth = False

        if data.theGoal.getColor() == data.playerOne.getColor():
            data.getGoal = True
            data.needsSwitch = False
        else:
            data.getGoal = False
            data.needsSwitch = True

def bestDistance(data):
    left = nextDistance(data,(-1, 0))
    right = nextDistance(data,(1, 0))
    up = nextDistance(data,(0, -1))
    down = nextDistance(data, (0, 1))
    best = (1000, (0,0))
    d = distance (data)

    if left < d and left < right and left < up and left < down or left < best[0]:
        x = data.playerTwo.getNextMoveLocation((-1,0))[0]
        y = data.playerTwo.getNextMoveLocation((-1,0))[1]
        if not (x < 25 or x > data.width - 35 or y < 150 or y > data.height -35):
            best = (left, (-1, 0))
    if right < d and right < left and right < up and right < down or right < best[0]:
        x = data.playerTwo.getNextMoveLocation((1,0))[0]
        y = data.playerTwo.getNextMoveLocation((1,0))[1]
        if not (x < 25 or x > data.width - 35 or y < 150 or y > data.height -35):
            best = (right, (1,0))
    if up < d and up < right and up < left and up < down or up < best[0]:
        x = data.playerTwo.getNextMoveLocation((0,-1))[0]
        y = data.playerTwo.getNextMoveLocation((0,-1))[1]
        if not (x < 25 or x > data.width - 35 or y < 150 or y > data.height -35):
            best = (up, (0,-1))
    if down < d and down < right and down < up and down < left or down < best[0]:
        x = data.playerTwo.getNextMoveLocation((0,1))[0]
        y = data.playerTwo.getNextMoveLocation((0,1))[1]
        if not (x < 25 or x > data.width - 35 or y < 150 or y > data.height -35):
            best = (down, (0,1))

    return best[1]

def nextDistance(data, d):
    if data.currentPlayer == 1:
        px = data.playerOne.getNextMoveLocation(d)[0]
        py = data.playerOne.getNextMoveLocation(d)[1]

    if data.currentPlayer == 0:
        px = data.playerTwo.getNextMoveLocation(d)[0]
        py = data.playerTwo.getNextMoveLocation(d)[1]

    if data.needsHealth and len(data.healths) != 0:
        for healthy in data.healths:
            sx = healthy.getLocation()[0]
            sy = healthy.getLocation()[1]
    elif data.getGoal:
        sx = data.theGoal.getLocation()[0]
        sy = data.theGoal.getLocation()[1]
    else:
        sx = data.theSwitchZone.getLocation()[0]
        sy = data.theSwitchZone.getLocation()[1]

    result = math.sqrt((sx - px)**2 + (sy - py)**2)
    return int(result)


def distance(data):
    if data.currentPlayer == 1:
        px = data.playerOne.getLocation()[0]
        py = data.playerOne.getLocation()[1]

    if data.currentPlayer == 0:
        px = data.playerTwo.getLocation()[0]
        py = data.playerTwo.getLocation()[1]

    if data.needsHealth and len(data.healths) != 0:
        for healthy in data.healths:
            sx = healthy.getLocation()[0]
            sy = healthy.getLocation()[1]
    elif data.getGoal:
        sx = data.theGoal.getLocation()[0]
        sy = data.theGoal.getLocation()[1]
    else:
        sx = data.theSwitchZone.getLocation()[0]
        sy = data.theSwitchZone.getLocation()[1]

    result = math.sqrt((sx - px)**2 + (sy - py)**2)
    return int(result)