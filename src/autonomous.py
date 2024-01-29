from vex import *
import time

# Stores each object's current position and associated functions
# X = x position, Y = y position, W = width, H = height
# F = associated callback function, S = signal required to run function (clicked, pressed, etc)
objectsXYWHSF = []


class V5GLError(Exception):\
    def __init__(self, message="Sorry, V5GL encountered an internal error."):
        self.message = message
        super().__init__(self.message)

class Autonomous():
    def __init__(self, bg="white", background="", refresh_rate=60):
        super().__init__(bg, background, refresh_rate)
        self.LoopSpeed = 0.1
        self.background = bg
        self.refreshRate = refresh_rate

    def AddObject(self, x, y, w, h, f, s):
        objectsXYWHSF.append([x, y, w, h, f, s])

    def ClearScreen(self):
        brain.screen.clear_screen()

    def SetBackground(self, bg):
        self.background = bg

    def SetRefreshRate(self, rate):
        self.refreshRate = rate

    def GetBackground(self):
        return self.background

    def GetRefreshRate(self):
        return self.refreshRate

    def GetObjectsXY(self):
        return objectsXY
    
    def 