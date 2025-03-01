from tkinter import *
from ioObjects import *
from playerObjects import *
from gamePlay import*
from automation import*
import random
import math

#draws all gameplay elements from playerObjects.py and ioObjects.py
#creates players and objects
#runs gamePlay.py and automation.py for rules and bot
#key control set up

def drawBoard():
    width = 720
    height = 720
    run(width, height)

def init(data):
    data.bgColor = "white"
    data.playerOneColor = "royalblue4"
    data.playerOneTrailColor = "royalblue1"
    data.playerTwoColor = "coral3"
    data.playerTwoTrailColor = "coral"
    data.healthColor = "lavenderblush3"
    data.flipColor = "powder blue"
    data.sideMargin = 25
    data.topMargin = 150
    data.time = 0
    data.cellSize = 4
    data.rows = 50 // data.cellSize
    data.cols = 50 // data.cellSize
    data.healths = set()
    data.flips = set()
    data.playerOnes = set()
    data.playerTwos = set()
    data.currentPlayer = 0
    # 0 = p1
    # 1 = p2
    #currentPlayer = user controlled
    data.maxHealth = 6
    data.playerOneHealth = data.maxHealth//2
    data.playerTwoHealth = data.maxHealth//2
    data.reducePlayerOneHealth = False
    data.reducePlayerTwoHealth = False
    data.switched = False
    data.canFlip = False
    data.playerSpeed = 10
    data.scoreValueP1 = 100
    data.scoreValueP2 = 100
    data.switch = False
    data.playerSet = set()
    data.getGoal = False
    data.gameOver = False
    data.needsSwitch = False
    data.needsHealth = False
    data.track = False

    scoreVars(data)
    healthVars(data)
    createGoal(data)
    createHealth(data)
    createFlip(data)
    createSwitchZone(data)
    createPlayerOne(data)
    createPlayerTwo(data)

def drawNewBoard(canvas, data):
    canvas.create_rectangle(
    data.sideMargin,
    data.topMargin,
    data.width - data.sideMargin,
    data.height - data.sideMargin,
    fill = None,
    outline = "Black")

def getRandomLocation(data):
    rowSize = data.rows * data.cellSize
    colSize = data.cols * data.cellSize
    x = random.randint(data.sideMargin, data.width - data.sideMargin - rowSize)
    y = random.randint(data.topMargin, data.height - data.sideMargin - colSize)
    return (x, y)

def createPlayerOne(data):
    data.playerOne = player(data.sideMargin, data.topMargin-10,
    data.playerOneColor, data.playerSpeed, (0, 1))

def createPlayerTwo(data):
    data.playerTwo = player(data.width-data.sideMargin, data.topMargin-10,
    data.playerTwoColor, data.playerSpeed, (0, 1))

def updateTrail(data):
    data.playerOneTrail = playerTrail(data.playerOne.getLocation()[0],
    data.playerOne.getLocation()[1], data.playerOneTrailColor, 0, (0,0))
    data.playerOnes.add(data.playerOneTrail)

    data.playerTwoTrail = playerTrail(data.playerTwo.getLocation()[0],
    data.playerTwo.getLocation()[1], data.playerTwoTrailColor, 0, (0,0))
    data.playerTwos.add(data.playerTwoTrail)

def createGoal(data):
    x = data.width//2
    y = data.height-25
    color = random.choice([data.playerOneColor, data.playerTwoColor])
    data.theGoal = goal(x, y, 0, color, data.bgColor, 10)

def createHealth(data):
    data.healthSpeed = 5
    x = getRandomLocation(data)[0]
    y = getRandomLocation(data)[1]
    data.healths.add(health(x, y, data.healthSpeed, data.healthColor, 10))

def createFlip(data):
    data.healthSpeed = 10
    x = getRandomLocation(data)[0]
    y = getRandomLocation(data)[1]
    data.flips.add(health(x, y, data.healthSpeed, data.flipColor, 10))

def flipBoard(data):
    if data.canFlip:
        data.playerOne.flip()
        data.playerTwo.flip()
        for p1 in data.playerOnes:
            p1.flip()
            data.canFlip = False
        for p2 in data.playerTwos:
            p2.flip()
            data.canFlip = False

def removeHealth(data):
   data.healths.clear()

def removeFlip(data):
    data.flips.clear()

def createSwitchZone(data):
    x = getRandomLocation(data)[0]
    y = getRandomLocation(data)[1]
    data.theSwitchZone = switchZone(x, y, 0, None, 50)

def scoreVars(data):
    if len(str(data.scoreValueP1)) == 1:
        data.scorePrintP1 = "000%d" %(data.scoreValueP1)
    if len(str(data.scoreValueP1)) == 2:
        data.scorePrintP1 = "00%d" %(data.scoreValueP1)
    if len(str(data.scoreValueP1)) == 3:
        data.scorePrintP1 = "0%d" %(data.scoreValueP1)
    if len(str(data.scoreValueP1)) == 4:
        data.scorePrintP1 = "%d" %(data.scoreValueP1)

    if len(str(data.scoreValueP2)) == 1:
        data.scorePrintP2 = "000%d" %(data.scoreValueP2)
    if len(str(data.scoreValueP2)) == 2:
        data.scorePrintP2 = "00%d" %(data.scoreValueP2)
    if len(str(data.scoreValueP2)) == 3:
        data.scorePrintP2 = "0%d" %(data.scoreValueP2)
    if len(str(data.scoreValueP2)) == 4:
        data.scorePrintP2 = "%d" %(data.scoreValueP2)

    if data.scoreValueP1 >= 1000 or data.scoreValueP1 >= 1000:
        data.gameOver = True

    if data.scoreValueP1 <= 0 or data.scoreValueP1 <= 0:
        data.gameOver = True

def drawTarget(canvas, data):
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

    if data.track:
        canvas.create_line(px, py, sx, sy)

def drawScore(canvas, data):
    #player one score
    canvas.create_text(675, 68, text = data.scorePrintP1, font = "Helvetica 20")
    #player two score
    canvas.create_text(675, 113, text = data.scorePrintP2, font = "Helvetica 20")

def healthVars(data):
    #calculating bar width from score
    data.p1barwidth = (data.width//2 // data.maxHealth)
    data.p1barwidth *= data.playerOneHealth
    #calculating bar width from score
    data.p2barwidth = (data.width//2 // data.maxHealth)
    data.p2barwidth *= data.playerTwoHealth

def drawHealth(canvas, data):
    #Player One Health
    canvas.create_rectangle(data.sideMargin, 60, data.width//2, 75, fill = None, outline = data.playerOneTrailColor)
    canvas.create_rectangle(data.sideMargin, 60, data.p1barwidth, 75, fill = data.playerOneTrailColor, outline = data.playerOneTrailColor)
    #Player Two Health
    canvas.create_rectangle(data.sideMargin, 105, data.width//2, 120, fill = None, outline = data.playerTwoTrailColor)
    canvas.create_rectangle(data.sideMargin, 105, data.p2barwidth, 120, fill = data.playerTwoTrailColor, outline = data.playerTwoTrailColor)

def drawCurrentPlayer(canvas, data):
    if data.currentPlayer == 0:
        x = data.playerOne.getLocation()[0] +3
        y = data.playerOne.getLocation()[1] +2
        x1 = data.playerOne.getLocation()[2] -2
        y1 = data.playerOne.getLocation()[3] -2

        canvas.create_rectangle(x, y, x1, y1, fill = "white", width = 0)

    if data.currentPlayer == 1:
        x = data.playerTwo.getLocation()[0] +3
        y = data.playerTwo.getLocation()[1] +2
        x1 = data.playerTwo.getLocation()[2] -2
        y1 = data.playerTwo.getLocation()[3] -2

        canvas.create_rectangle(x, y, x1, y1, fill = "white", width = 0)

def drawGameOver(canvas,data):
    if data.gameOver == True:
        canvas.create_rectangle(0, 0, data.width, data.height, fill = data.bgColor)
        canvas.create_text(data.width//2, data.topMargin, text = "GAME OVER", font = "Helvetica 70")
        if data.scoreValueP1 > data.scoreValueP2:
            s = "%s wins with %d points" %("Player One", data.scoreValueP1)
        if data.scoreValueP2 > data.scoreValueP1:
            s = "%s wins with %d points" %("Player Two", data.scoreValueP2)
        else: s = "Tie"
        canvas.create_text(data.width//2, data.height//2, text = s, font = "Helvetica 40")
        canvas.create_text(data.width//2, data.width-data.topMargin, text = "press r to restart", font = "Helvetica 20")

def motion(canvas, event, data):
    pass

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if (event.keysym == "space" and data.switched == False and data.switch
        or data.needsSwitch and data.switched == False and data.switch):
        data.switched = True
        data.switch = False
        data.needsSwitch = False
        if data.currentPlayer != 1:
            data.currentPlayer = 1
        else: data.currentPlayer = 0
    elif (event.keysym == "space" and data.switched and data.switch
          or data.needsSwitch and data.switched and data.switch):
        data.switched = False
        data.switch = False
        data.needsSwitch = False
        if data.currentPlayer != 1:
            data.currentPlayer = 1
        else: data.currentPlayer = 0
    else: data.switch = False

    if event.keysym == "Up":
        if not data.switched:
            data.playerOne.changeDirection((0, -1))
        else:
            data.playerTwo.changeDirection((0, -1))
    if event.keysym == "Left":
        if not data.switched:
            data.playerOne.changeDirection((-1, 0))
        else:
            data.playerTwo.changeDirection((-1, 0))
    if event.keysym == "Down":
        if not data.switched:
            data.playerOne.changeDirection((0, 1))
        else:
            data.playerTwo.changeDirection((0, 1))
    if event.keysym == "Right":
        if not data.switched:
            data.playerOne.changeDirection((1, 0))
        else:
            data.playerTwo.changeDirection((1, 0))
    elif event.keysym == "r" and data.gameOver:
        init(data)

    #testing
    if event.keysym == "g":
        data.gameOver = True
    if event.keysym == "f":
        data.canFlip = True
    if event.keysym == "t":
        data.track = True

def timerFired(data):
    data.time += data.timerDelay
    scoreVars(data)
    morePointsP1(data)
    morePointsP2(data)
    canSwitch(data)
    crash(data)
    automatedDirection(data)
    flipBoard(data)

    if canFlipP1(data):
        data.canFlip = True
        removeFlip(data)

    if canFlipP2(data):
        data.canFlip = True
        removeFlip(data)

    if data.time % 100 == 0:
        data.playerOne.move()
        data.playerTwo.move()
        updateTrail(data)

        #update health
        if moreHealthP1(data):
            if data.playerOneHealth < data.maxHealth:
                data.playerOneHealth+=1
            healthVars(data)
            removeHealth(data)

        if data.reducePlayerOneHealth and data.playerOneHealth > 1:
            data.playerOneHealth-=1
            healthVars(data)
            data.reducePlayerOneHealth = False
        elif data.reducePlayerOneHealth and data.playerOneHealth ==1:
            data.gameOver = True

        if moreHealthP2(data):
            if data.playerTwoHealth < data.maxHealth:
                data.playerTwoHealth+=1
            healthVars(data)
            removeHealth(data)


        if data.reducePlayerTwoHealth and data.playerTwoHealth > 1:
            data.playerTwoHealth-=1
            healthVars(data)
            data.reducePlayerTwoHealth = False
        elif data.reducePlayerTwoHealth and data.playerTwoHealth ==1:
            data.gameOver = True

    for healthy in data.healths:
        healthy.move(1, 0)

    # spawn more health every 10 seconds if health is less than 2
    if data.playerTwoHealth < 2 or data.playerOneHealth < 2:
        if data.time % 10000 == 0:
            createHealth(data)
            createFlip(data)

    if data.time % 5000 == 0:
        #every 5 seconds make a new switch zone
        createSwitchZone(data)

    #every 8 seconds create a new goal color
    if data.time % 8000 == 0:
        createGoal(data)

def redrawAll(canvas, data):

    for healthy in data.healths:
        healthy.draw(canvas)

    for flipy in data.flips:
        flipy.draw(canvas)

    for p1 in data.playerOnes:
        p1.draw(canvas)
    data.playerOne.draw(canvas)

    for p2 in data.playerTwos:
        p2.draw(canvas)
    data.playerTwo.draw(canvas)

    drawScore(canvas, data)

    drawHealth(canvas, data)

    data.theSwitchZone.draw(canvas)

    drawNewBoard(canvas, data)

    data.theGoal.draw(canvas)

    drawCurrentPlayer(canvas, data)

    drawGameOver(canvas, data)

    drawTarget(canvas, data)

####################################
# borrowed from 15-112 Animation Starter Code
####################################
#
def run(width, height):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill=data.bgColor, width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    root.bind('<Motion>', lambda event:
                            motion(canvas, event, data))
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
