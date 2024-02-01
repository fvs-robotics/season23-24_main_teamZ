"""
This main program defines autonomous and driver control functions to handle
motor movements, arm control, intake control, and launcher control.

During autonomous mode, the robot will perform predefined actions.
During driver control mode, use the controller to manually control the robot.

Ensure all hardware components are properly connected and configured before running the program.

Date: 2023-2024. January 2024.
"""

import sys
import vex
from vex import *
import urandom

brain = Brain()

# region config
controller = Controller(PRIMARY)  # Primary controller
motor_left_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)  # Left front motor
motor_right_front = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)  # Right front motor
motor_left_back = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)  # Left back motor
motor_right_back = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)  # Right back motor
arm_left = Motor(Ports.PORT11, GearSetting.RATIO_36_1, False)  # Left arm motor
arm_right = Motor(Ports.PORT20, GearSetting.RATIO_36_1, False)  # Right arm motor
intake = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)  # Intake motor
launcher = Motor(Ports.PORT6, GearSetting.RATIO_36_1, False)  # Launcher motor


# end of region config

def initialize_autonomous():
    # start the autonomous control tasks
    _autonomous_thread = Thread(autonomous)
    # wait for the driver control period to end
    while (competition.is_autonomous() and competition.is_enabled()):
        # wait 10 milliseconds before checking again
        wait(10, MSEC)
    # stop the autonomous control tasks
    _autonomous_thread.stop()


def autonomous():
    # Set the velocity of four motors to full PERCENT.
    full = 100
    motor_left_front.set_velocity(full, PERCENT)
    motor_right_front.set_velocity(full, PERCENT)
    motor_left_back.set_velocity(full, PERCENT)
    motor_right_back.set_velocity(full, PERCENT)

    # Set the maximum torque of four motors to full PERCENT.
    # The intake wheels always spin.
    motor_left_front.set_max_torque(full, PERCENT)
    motor_right_front.set_max_torque(full, PERCENT)
    motor_left_back.set_max_torque(full, PERCENT)
    motor_right_back.set_max_torque(full, PERCENT)
    intake.spin(FORWARD, full, PERCENT)

    # left motor in REVERSE direction
    # right motor in FORWARD direction

    # when the robot starts in the left corner
    while True:
        # release the intake to the horizon
        arm_left.spin(FORWARD)
        arm_right.spin(REVERSE)
        wait(1, SECONDS)
        arm_left.stop(HOLD)
        arm_right.stop(HOLD)

        # lift the intake arm first
        arm_left.spin_for(REVERSE, 30, DEGREES)
        arm_right.spin_for(FORWARD, 30, DEGREES)

        # turn right
        motor_left_front.spin(REVERSE)
        motor_left_back.spin(REVERSE)
        motor_right_front.spin(FORWARD)
        motor_right_back.spin(FORWARD)
        wait(1, SECONDS)
        motor_left_front.stop()
        motor_left_back.stop()
        motor_right_front.stop()
        motor_right_back.stop()

    # 插片程序


def initialize_driver_control():
    # start the driver control tasks
    _driver_thread = Thread(driver_control)

    # wait for the driver control period to end
    while (competition.is_driver_control() and competition.is_enabled()):
        # wait 10 milliseconds before checking again
        wait(10, MSEC)

    # stop the driver control tasks
    _driver_thread.stop()


def driver_control():
    full = 100
    intake.spin(FORWARD, full, PERCENT)
    # place drive control code here, inside the loop
    while True:
        # This is the main loop for the driver control.
        # Each time through the loop you should update motor
        # movements based on input from the controller.

        # Temperature return:
        # Every movement will return the temperature of the motor on the brain screen.
        tempArmL = arm_left.temperature()
        tempArmR = arm_right.temperature()
        brain.screen.clear_screen()
        brain.screen.print(tempArmL)
        brain.screen.print(tempArmR)

        # Controller Axis 1 and Axis 3:
        # The left front motor and left back motor spin forward when pushing the left joystick forward.
        # Then, the left front motor and left back motor spin backward when pushing the left joystick backward.
        motor_left_front.spin(REVERSE, controller.axis1.value() + controller.axis3.value(), PERCENT)
        motor_left_back.spin(REVERSE, controller.axis1.value() + controller.axis3.value(), PERCENT)
        motor_right_front.spin(REVERSE, controller.axis1.value() - controller.axis3.value(), PERCENT)
        motor_right_back.spin(REVERSE, controller.axis1.value() - controller.axis3.value(), PERCENT)

        # R1 and R2 buttons:
        # The right arm motor and left arm motor lift up the arms at once when pressing the R1 button.
        # Then, the right arm motor and left arm motor lift down the arms at once when pressing the R2 button.
        if controller.buttonL1.pressing():
            arm_left.spin_for(REVERSE, full, PERCENT)
            arm_right.spin_for(FORWARD, full, PERCENT)
            wait(0.5, SECONDS)

        elif controller.buttonL2.pressing():
            arm_left.spin_for(FORWARD, full, PERCENT)
            arm_right.spin_for(REVERSE, full, PERCENT)
            wait(0.5, SECONDS)

        elif controller.buttonR1.pressing():
            intake.spin(REVERSE, full, PERCENT)

        elif controller.buttonR2.pressing():
            intake.spin(FORWARD, full, PERCENT)

        if controller.buttonUp.pressing():
            launcher.spin(FORWARD, full, PERCENT)

        if controller.buttonDown.pressing():
            launcher.set_position(0, DEGREES)
            launcher.stop(HOLD)

        else:
            # Stop the arms only if neither ButtonL2 nor ButtonL1 is pressed
            arm_left.stop(HOLD)
            arm_right.stop(HOLD)
            wait(20, MSEC)


# allows access to Competition methods
competition = Competition(driver_control, autonomous)