from vex import *
import time

# Stores each object's current position and associated functions
# X = x position, Y = y position, W = width, H = height
# F = associated callback function, S = signal required to run function (clicked, pressed, etc)
objectsXYWHSF = []


class V5GLError(Exception):
    def __init__(self, message="Sorry, V5GL encountered an internal error."):
        self.message = message
        super().__init__(self.message)


class V5Application:
    # bg and background are different names for the same thing, both will produce desired result.
    # Refresh rate determines the screen refresh rate in hertz
    def __init__(self, bg="white", background="", refresh_rate=60):
        self.LoopSpeed = None
        self.background = bg
        if not background == "":
            self.background = background
            self.refreshRate = refresh_rate

    def Run(self):
        # This is the main loop of the GUI
        self.lastPressX = None
        self.lastPressY = None

        while True:
            self.pressX = brain.screen.x_position()
            self.pressY = brain.screen.y_position()

            # Test if the screen has been touched and if so, get the coordinates of the touch
            if self.pressX != self.lastPressX or self.pressY != self.lastPressY:
                self.lastPressX = self.pressX
                self.lastPressY = self.pressY

                for object in objectsXY:
                    if self.pressX <= object[0] + object[2] and self.pressX >= object[0] and self.pressY <= object[1] + \
                            object[3] and self.pressY >= object[1]:
                        object[4]()

            # If the loop is running at a faster rate than the screen refresh rate, then wait until the next screen refresh
            if self.LoopSpeed != None:
                if self.LoopSpeed > self.refreshRate:
                    time.sleep(self.LoopSpeed / self.refreshRate)
                else:
                    time.sleep(1 / self.refreshRate)
            else:
                time.sleep(1 / self.refreshRate)

            self.lastPressX = pressX
            self.lastPressY = pressY

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
