import sys
import vex
from vex import *
import motor_group
import drivetrain
import smartdrive

# region config
brain = vex.Brain()
mLF = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, True)  # Left front motor
mRF = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)  # Right front motor
mLB = vex.Motor(vex.Ports.PORT3, vex.GearSetting.RATIO18_1, True)  # Left back motor
mRB = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO18_1, True)  # Right back motor
armL = vex.Motor(vex.Ports.PORT5, vex.GearSetting.RATIO36_1, True)  # Left arm motor
armR = vex.Motor(vex.Ports.PORT6, vex.GearSetting.RATIO36_1, True)  # Right arm motor
intake = vex.Motor(vex.Ports.PORT8, vex.GearSetting.RATIO18_1, True)  # Intake motor
controller1 = vex.Controller(vex.Ports.PORT9, vex.ControllerType.PRIMARY, True)  # Primary controller
inertia_center = vex.Inertial(vex.Ports.PORT21)  # Inertial sensor
# endregion config


# Creates a competition object that allows access to Competition methods.
# This creates a global instance.
competition = vex.Competition()


def pre_auton():
    pass


def autonomous():
    # Place autonomous code here

    pass


def drivercontrol():
    # Place drive control code here, inside the loop
    while True:
        # This is the main loop for the driver control.
        # Each time through the loop you should update motor
        # movements based on input from the controller.

        intake.spin(reverse, 100, percent)

        """
        Temperature return:
        Every movement will return the temperature of the motor on the brain screen.
        """
        tempArmL = armL.temperature(CELCIUS)
        tempArmR = armR.temperature(CELCIUS)
        brain.screen.clear_screen()
        brain.screen.print_(tempArmL, TRUE)
        brain.screen.print_(tempArmR, TRUE)

        """
        Controller Axis 1 and Axis 3:
        The left front motor and left back motor spin forward when pushing the left joystick forward.
        Then, the left front motor and left back motor spin backward when pushing the left joystick backward.
        """
        mLF.spin(FWD, controller1.axis3.value() + controller1.axis1.value(), PCT)
        mLB.spin(FWD, controller1.axis3.value() + controller1.axis1.value(), PCT)
        mRF.spin(FWD, controller1.axis3.value() - controller1.axis1.value(), PCT)
        mRB.spin(FWD, controller1.axis3.value() - controller1.axis1.value(), PCT)

        """
        R1 and R2 buttons:
        The right arm motor and left arm motor lift up the arms at once when pressing the R1 button.
        Then, the right arm motor and left arm motor lift down the arms at once when pressing the R2 button.
        
        For reference, in vex.Motor class:
        def vex.Motor.spin_for_time	(self,
                                    direction,
                                    time,
                                    timeUnits = TimeUnits.SEC,
                                    velocity = None,
                                    velocityUnits = VelocityUnits.PCT
                                    )
        """

        if controller1.ButtonR1.pressing():
            armL.spin_for_time(FWD, 300, MSEC, 100, PCT)
            armR.spin_for_time(FWD, 300, MSEC, 100, PCT)
        if controller1.ButtonR2.pressing():
            armL.spin_for_time(REV, 300, MSEC, 100, PCT)
            armR.spin_for_time(REV, 300, MSEC, 100, PCT)
        else:
            armL.stop(hold)
            armR.stop(hold)

        # Sleep the task for a short amount of time to
        # prevent wasted resources.
        time.sleep(20 / 1000)
        pass


# Do not adjust the lines below

# Set up (but don't start) callbacks for autonomous and driver control periods.
competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)

# Run the pre-autonomous function.
pre_auton()

# Initial actions.
# This is a placeholder code.
armL.spin(FWD, 20, PCT)
armR.spin(FWD, 20, PCT)
time.sleep(20 / 1000)
# End of placeholder code.

# Prevent main from exiting with an infinite loop.
while True:
    time.sleep(1)  # Placeholder code. Replace with the control code.

# Robot Mesh Studio runtime continues to run until all threads and
# competition callbacks are finished.
