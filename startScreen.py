from tkinter import *
from drawBoard import*
import random

#sets up start screen with about and levels
#if user presses start, drawBoard is called
#draw board is a seperate file that runs the game

def startScreen():
    width = 720
    height = 720
    run(width, height)

def init(data):
    data.start = False
    startScreenVars(data)
    levelsScreenVars(data)
    aboutScreenVars(data)
    data.playerOne = player(25, 25, "Black", 10, (0, 1))
    data.playerTwo = player(data.width//2, 25, "Black", 10, (0, 1))
    data.playerThree = player(data.width-25, 25, "Black", 10, (0, 1))
    data.goHome = False

def startScreenVars(data):
    data.bgColor = "white"
    data.highlightColor = "royalblue1"
    data.defaultColor = data.bgColor
    data.margin = 80
    data.boxWidth = (data.width - data.margin) // 3
    startScreenStart(data)
    startScreenLevels(data)
    startScreenAbout(data)

def startScreenStart(data):
    data.startBoxColor = data.defaultColor
    data.startBoxX0 = data.margin
    data.startBoxY0 = data.height - data.margin*2
    data.startBoxX1 = data.boxWidth
    data.startBoxY1 = data.height-data.margin
    data.startBoxCenterX = (data.startBoxX0 + data.startBoxX1) //2
    data.startBoxCenterY = (data.startBoxY0 + data.startBoxY1) //2

def startScreenLevels(data):
    data.levelsBoxColor = data.defaultColor
    data.levelsBoxX0 = data.margin + data.boxWidth
    data.levelsBoxY0 = data.height - data.margin*2
    data.levelsBoxX1 = data.boxWidth*2
    data.levelsBoxY1 = data.height-data.margin
    data.levelsBoxCenterX = (data.levelsBoxX0 + data.levelsBoxX1) //2
    data.levelsBoxCenterY = (data.levelsBoxY0 + data.levelsBoxY1) //2

def startScreenAbout(data):
    data.aboutBoxColor = data.defaultColor
    data.aboutBoxX0 = data.margin + data.boxWidth*2
    data.aboutBoxY0 = data.height - data.margin*2
    data.aboutBoxX1 = data.boxWidth*3
    data.aboutBoxY1 = data.height-data.margin
    data.aboutBoxCenterX = (data.aboutBoxX0 + data.aboutBoxX1) //2
    data.aboutBoxCenterY = (data.aboutBoxY0 + data.aboutBoxY1) //2

def drawStartScreen(canvas, data):
    #background of start screen
    canvas.create_rectangle(0,0, data.width, data.height, fill = data.bgColor)
    drawStartScreenStart(canvas, data)
    drawStartScreenLevels(canvas, data)
    drawStartScreenAbout(canvas, data)

def drawStartScreenStart(canvas, data):
    #start button
    canvas.create_rectangle(
    data.startBoxX0,
    data.startBoxY0,
    data.startBoxX1,
    data.startBoxY1,
    fill = data.startBoxColor,
    outline = data.startBoxColor)
    canvas.create_text(
    data.startBoxCenterX,
    data.startBoxCenterY,
    text = "START",
    font = "Helvetica 20")

def drawStartScreenLevels(canvas, data):
    #levels button
    canvas.create_rectangle(
    data.levelsBoxX0,
    data.levelsBoxY0,
    data.levelsBoxX1,
    data.levelsBoxY1,
    fill = data.levelsBoxColor,
    outline = data.levelsBoxColor)
    canvas.create_text(
    data.levelsBoxCenterX,
    data.levelsBoxCenterY,
    text = "HOW TO",
    font = "Helvetica 20")

def drawStartScreenAbout(canvas, data):
    #about button
    canvas.create_rectangle(
    data.aboutBoxX0,
    data.aboutBoxY0,
    data.aboutBoxX1,
    data.aboutBoxY1,
    fill = data.aboutBoxColor,
    outline = data.aboutBoxColor)
    canvas.create_text(
    data.aboutBoxCenterX,
    data.aboutBoxCenterY,
    text = "ABOUT",
    font = "Helvetica 20")

def levelsScreenVars(data):
    data.levels = False

def drawLevelsScreen(canvas, data):
    #background of levels screen
    canvas.create_rectangle(0,0, data.width, data.height,
    fill = data.highlightColor)
    canvas.create_text(data.width//2, (data.height//2)-50 ,
    text = "1. Use arrow keys to move player", font = "Helvetica 20")
    canvas.create_text(data.width//2, (data.height//2)+50,
    text = "2. Press space to switch players", font = "Helvetica 20")
    canvas.create_rectangle(10, 10, 50, 50)
    canvas.create_text(30, 30, text = "'' B ''", font = "Helvetica 15")
def aboutScreenVars(data):
    data.about = False

def drawAboutScreen(canvas, data):
    #background of about screen
    canvas.create_rectangle(0,0, data.width, data.height, fill = data.highlightColor)
    canvas.create_text(data.width//2, data.height//2, text = "Game created by Eli King for 15-112 Summer 2019.", font = "Helvetica 20")
    canvas.create_rectangle(10, 10, 50, 50)
    canvas.create_text(30, 30, text = "'' B ''", font = "Helvetica 15")

def motion(canvas, event, data):
    x, y = event.x, event.y
    if (x > data.startBoxX0 and x < data.startBoxX1
    and y > data.startBoxY0 and y < data.startBoxY1):
        data.startBoxColor = data.highlightColor
    else: data.startBoxColor = data.defaultColor
    if (x > data.levelsBoxX0 and x < data.levelsBoxX1
    and y > data.levelsBoxY0 and y < data.levelsBoxY1):
        data.levelsBoxColor = data.highlightColor
    else: data.levelsBoxColor = data.defaultColor
    if (x > data.aboutBoxX0 and x < data.aboutBoxX1
    and y > data.aboutBoxY0 and y < data.aboutBoxY1):
        data.aboutBoxColor = data.highlightColor
    else: data.aboutBoxColor = data.defaultColor

def mousePressed(event, data):
    x, y = event.x, event.y
    if (x > data.startBoxX0 and x < data.startBoxX1
    and y > data.startBoxY0 and y < data.startBoxY1):
        data.start = True
    if (x > data.levelsBoxX0 and x < data.levelsBoxX1
    and y > data.levelsBoxY0 and y < data.levelsBoxY1):
        pass
        data.levels = True
    if (x > data.aboutBoxX0 and x < data.aboutBoxX1
    and y > data.aboutBoxY0 and y < data.aboutBoxY1):
        pass
        data.about = True

def keyPressed(event, data):
    if event.keysym == "b":
        data.goHome = True
    else: data.goHome = False

def timerFired(data):
    data.playerOne.move()
    data.playerTwo.move()
    data.playerThree.move()
    d = random.choice([(0, 1), (0, -1), (1, 0),(-1, 0)])
    d1 = random.choice([(0, 1), (0, -1), (1, 0),(-1, 0)])
    d2 = random.choice([(0, 1), (0, -1), (1, 0),(-1, 0)])
    data.playerOne.changeDirection((d))
    data.playerTwo.changeDirection((d1))
    data.playerThree.changeDirection((d2))
    if data.goHome:
        init(data)

def redrawAll(canvas, data):
    if not data.start and not data.levels and not data.about:
        drawStartScreen(canvas, data)
        data.playerOne.draw(canvas)
        data.playerTwo.draw(canvas)
        data.playerThree.draw(canvas)
    if data.levels:
        drawLevelsScreen(canvas, data)
    if data.about:
        drawAboutScreen(canvas, data)
    if data.start:
        canvas.create_text(data.width//2, data.height//2,
        text = "close window to start game", font = "Helvetica 20")


####################################
# borrowed from 15-112 Animation Starter Code
####################################

def run(width, height):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill= data.bgColor, width=0)
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

startScreen()
drawBoard()
