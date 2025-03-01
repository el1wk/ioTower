from tkinter import *
import random

#goal, health, flip zone, and flip objects are controlled here

class io (object):
    def __init__(self, x, y, speed, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.width = 720
        self.height = 720

    def draw(self, canvas):
        canvas.create_rectangle(
        self.x,
        self.y,
        self.x+self.size,
        self.y+self.size,
        fill = self.color,
        outline = self.color)

    def __hash__(self):
        return hash((self.x, self.y, self.speed, self.color, self.size))

    def isCollision(self, x, y):
        if (x >= self.x and x <= self.x + self.size
        and y >= self.y and y <= self.y + self.size):
            return True
        return False

    def getLocation(self):
        x = self.x
        y = self.y
        x1 = self.x+self.size
        y1 = self.y+self.size
        return (x, y, x1, y1)

class goal (io):
    def __init__(self, x, y, speed, color, outlineColor, size):
        super().__init__(x, y, speed, color, size)
        self.outlineColor = outlineColor

    def draw(self, canvas):
        canvas.create_oval(
        self.x-self.size,
        self.y-self.size,
        self.x+self.size,
        self.y+self.size,
        fill = self.color,
        outline = self.outlineColor,
        width = 5)

    def getColor(self):
        return self.color

    def changeColor(self, newColor):
        self.color = newColor

    def flip(self):
        self.y = 150

class health (io):
    def __init__(self, x, y, speed, color, size):
        super().__init__(x, y, speed, color, size)

    def move(self, x, y):
        #move back and forth
        if self.x < 25:
            self.speed*= -1
        if self.x+self.size > self.width - 25:
            self.speed*= -1
        self.x += (x*self.speed)

    def speedUp(self, n):
        self.speed = n

class flip (io):
    def __init__(self, x, y, speed, color, size):
        super().__init__(x, y, speed, color, size)

    def move(self, x, y):
        #move back and forth
        if self.x < 25:
            self.speed*= -1
        if self.x+self.size > self.width - 25:
            self.speed*= -1
        self.y += (y*self.speed)

    def speedUp(self, n):
        self.speed = n

class switchZone(io):
    def __init__(self, x, y, speed, color, size):
        super().__init__(x, y, speed, color, size)
        #stipple density
        self.cellSize = 2
        #keeps consistant size depending on density or transparency
        self.rows = 50 // self.cellSize
        self.cols = 50 // self.cellSize

        self.switchZone = [([None]*self.cols) for row in range(self.rows)]

    def draw(self, canvas):
        canvas.create_rectangle(
        self.x,
        self.y,
        self.x+self.size,
        self.y+self.size,
        fill = None,
        outline = None,
        width = 0)

        for i in range(len(self.switchZone)):
            for j in range(len(self.switchZone[0])):
                if i % 3 == 0 and j % 3 == 0:
                    #sets overy other other within grid to be black
                    self.switchZone[i][j] = "gray20"
                switchZone.drawStipple(self, canvas, i, j, self.switchZone[i][j])

    def drawStipple(self, canvas, rows, cols, color):
        left = self.x + self.cellSize*cols
        top = self.y + self.cellSize*rows
        right = left + self.cellSize
        bottom = top + self.cellSize
        canvas.create_oval(
        left, top, right, bottom,
        fill = color,
        width = 0)

        canvas.create_rectangle(
        self.x,
        self.y,
        self.x+self.size,
        self.y+self.size,
        fill = None,
        width = 0)