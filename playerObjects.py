import random

#player class controls players on screen
#player trail is a list of the player's previous locations

class player (object):
    def __init__(self, x, y, color, speed, direction):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.direction = direction
        self.size = 10
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

    def move(self):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

        if self.x < 25:
            self.x = 25

        if self.y < 150:
            self.y = 150

        if self.x+self.size > self.width - 25-self.size:
            self.x = self.width - 25 - self.size

        if self.y +self.size > self.height - 25:
            self.y = self.height - 25 - self.size

    def increaseSpeed(self):
        self.speed +=5

    def changeDirection(self, d):
        self.direction = d

    def getLocation(self):
        x = self.x
        y = self.y
        x1 = self.x+self.size
        y1 = self.y+self.size
        return (x, y, x1, y1)


    def getNextMoveLocation(self, d):
        x = self.x + d[0]
        y = self.y + d[1]
        x1 = self.x+self.size
        y1 = self.y+self.size
        return (x, y, x1, y1)

    def getColor (self):
        return self.color

    def flip (self):
        #self.x = self.width-self.x - self.size
        self.y = (self.height + 150 - 25)- self.y - self.size

    def __hash__(self):
        return hash((self.x, self.y, self.color, self.speed, self.direction))

class playerTrail(player):
    def __init__(self, x, y, color, speed, direction):
        super().__init__(x, y, color, speed, direction)
        self.size = 10

    def draw(self, canvas):
        canvas.create_rectangle(
        self.x,
        self.y,
        self.x+self.size,
        self.y+self.size,
        fill = self.color,
        outline = self.color)

    def isCollision(self, x, y):
        if (x >= self.x and x <= self.x + self.size
        and y >= self.y and y <= self.y + self.size):
            return True
        return False