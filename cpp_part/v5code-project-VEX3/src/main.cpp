/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       VEX                                                       */
/*    Created:      Thu Sep 26 2019                                           */
/*    Description:  Competition Template                                      */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// LFmotor              motor         1               
// LBmotor              motor         12              
// RFmotor              motor         10              
// RBmotor              motor         19              
// LArm                 motor         11              
// RArm                 motor         20              
// Intake               motor         8               
// Launcher             motor         6               
// JumpA                digital_in    A               
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;

// A global instance of competition
competition Competition;

// define your global instances of motors and other devices here

/*---------------------------------------------------------------------------*/
/*                          Pre-Autonomous Functions                         */
/*                                                                           */
/*  You may want to perform some actions before the competition starts.      */
/*  Do them in the following function.  You must return from this function   */
/*  or the autonomous and usercontrol tasks will not be started.  This       */
/*  function is only called once after the V5 has been powered on and        */
/*  not every time that the robot is disabled.                               */
/*---------------------------------------------------------------------------*/

void pre_auton(void) {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();

  // All activities that occur before the competition starts
  // Example: clearing encoders, setting servo positions, ...
}

/*---------------------------------------------------------------------------*/
/*                                                                           */
/*                              Autonomous Task                              */
/*                                                                           */
/*  This task is used to control your robot during the autonomous phase of   */
/*  a VEX Competition.                                                       */
/*                                                                           */
/*  You must modify the code to add your own robot specific commands here.   */
/*---------------------------------------------------------------------------*/

void autonomous(void) {
//Segment 1

  LArm.spin(forward, 100, percent);
  RArm.spin(reverse, 100, percent);
  wait(0.3, sec);

  LArm.spin(reverse, 100, percent);
  RArm.spin(forward, 100, percent);
  wait(0.3, sec);

  Intake.spin(forward, 100, percent);
  wait(0.2, sec);

  LFmotor.spin(reverse, 100, percent);
  LBmotor.spin(reverse, 100, percent);
  RFmotor.spin(forward, 100, percent);
  RBmotor.spin(forward, 100, percent);
  wait(0.3,sec);

  LFmotor.stop(hold);
  RFmotor.stop(hold);
  LBmotor.stop(hold);
  RBmotor.stop(hold);
  wait(0.05, sec);

//Segment 2

  LFmotor.spin(reverse, 80, percent);
  LBmotor.spin(reverse, 80, percent);
  RFmotor.spin(reverse, 80, percent);
  RBmotor.spin(reverse, 80, percent);
  wait(0.2, sec);

  LFmotor.spin(reverse, 100, percent);
  LBmotor.spin(reverse, 100, percent);
  RFmotor.spin(forward, 100, percent);
  RBmotor.spin(forward, 100, percent);
  wait(0.48, sec);

  LFmotor.spin(forward, 100, percent);
  LBmotor.spin(forward, 100, percent);
  RFmotor.spin(forward, 100, percent);
  RBmotor.spin(forward, 100, percent);
  wait(0.33, sec);

  LFmotor.stop(hold);
  RFmotor.stop(hold);
  LBmotor.stop(hold);
  RBmotor.stop(hold);
  wait(0.01,sec);

  LArm.spin(forward, 100, percent);
  RArm.spin(reverse, 100, percent);
  wait(0.3, sec);

  LFmotor.spin(reverse, 100, percent);
  LBmotor.spin(reverse, 100, percent);
  RFmotor.spin(forward, 100, percent);
  RBmotor.spin(forward, 100, percent);
  wait(0.52, sec);

  LFmotor.stop(hold);
  RFmotor.stop(hold);
  LBmotor.stop(hold);
  RBmotor.stop(hold);
  wait(0.01,sec);


//Segment 3

  LFmotor.spin(reverse, 100, percent);
  LBmotor.spin(reverse, 100, percent);
  RFmotor.spin(forward, 100, percent);
  RBmotor.spin(forward, 100, percent);
  wait(0.52,sec);

  LFmotor.spin(forward, 70, percent);
  LBmotor.spin(forward, 70, percent);
  RFmotor.spin(reverse, 70, percent);
  RBmotor.spin(reverse, 70, percent);
  wait(0.27,sec);

  LArm.spin(reverse, 100, percent);
  RArm.spin(forward, 100, percent);
  wait(0.6,sec);

  LFmotor.stop(brake);
  RFmotor.stop(brake);
  LBmotor.stop(brake);
  RBmotor.stop(brake);
  wait(0.1, sec);


  //Segment 4

  LFmotor.spin(forward, 80, percent);
  LBmotor.spin(forward, 80, percent);
  RFmotor.spin(forward, 80, percent);
  RBmotor.spin(forward, 80, percent);
  wait(0.34,sec);

  LFmotor.spin(reverse, 100, percent);
  LBmotor.spin(reverse, 100, percent);
  RFmotor.spin(forward, 100, percent);
  RBmotor.spin(forward, 100, percent);
  wait(0.1,sec);

  Intake.spin(forward, 100, percent);
  wait(0.3,sec);

  LFmotor.spin(reverse, 70, percent);
  LBmotor.spin(reverse, 70, percent);
  RFmotor.spin(reverse, 70, percent);
  RBmotor.spin(reverse, 70, percent);
  wait(0.07,sec);

  LFmotor.spin(reverse, 100, percent);
  LBmotor.spin(reverse, 100, percent);
  RFmotor.spin(forward, 100, percent);
  RBmotor.spin(forward, 100, percent);
  wait(0.9,sec);

  LFmotor.stop(hold);
  RFmotor.stop(hold);
  LBmotor.stop(hold);
  RBmotor.stop(hold);
  wait(0.01,sec);


  //Segment 5

  LFmotor.spin(reverse, 100, percent);
  LBmotor.spin(reverse, 100, percent);
  RFmotor.spin(reverse, 100, percent);
  RBmotor.spin(reverse, 100, percent);
  wait(0.488, sec);

  LFmotor.spin(reverse, 90, percent);
  LBmotor.spin(reverse, 90, percent);
  RFmotor.spin(forward, 90, percent);
  RBmotor.spin(forward, 90, percent);
  wait(0.1,sec);

  LArm.spin(forward, 85, percent);
  RArm.spin(reverse, 85, percent);
  wait(0.4, sec);

  LFmotor.spin(reverse, 100, percent);
  LBmotor.spin(reverse, 100, percent);
  RFmotor.spin(forward, 100, percent);
  RBmotor.spin(forward, 100, percent);
  wait(0.8,sec);

  LFmotor.stop(brake);
  RFmotor.stop(brake);
  LBmotor.stop(brake);
  RBmotor.stop(brake);
  wait(0.01,sec);

  //Segment 6 

  LFmotor.stop(hold);
  RFmotor.stop(hold);
  LBmotor.stop(hold);
  RBmotor.stop(hold);
  LArm.stop(hold);
  RArm.stop(hold);

  LFmotor.spin(forward, 80, percent);
  LBmotor.spin(forward, 80, percent);
  RFmotor.spin(forward, 80, percent);
  RBmotor.spin(forward, 80, percent);
  wait(0.3, sec);

  LArm.spin(reverse, 85, percent);
  RArm.spin(forward, 85, percent);
  wait(0.4, sec);



  LFmotor.stop(hold);
  RFmotor.stop(hold);
  LBmotor.stop(hold);
  RBmotor.stop(hold);
  LArm.stop(hold);
  RArm.stop(hold);
  wait(0.01,sec);

}

/*---------------------------------------------------------------------------*/
/*                                                                           */
/*                              User Control Task                            */
/*                                                                           */
/*  This task is used to control your robot during the user control phase of */
/*  a VEX Competition.                                                       */
/*                                                                           */
/*  You must modify the code to add your own robot specific commands here.   */
/*---------------------------------------------------------------------------*/

void usercontrol(void) {
  // User control code here, inside the loop
  while (1) {
    LFmotor.spin(reverse, (Controller1.Axis1.value() + Controller1.Axis3.value()), percent);
    LBmotor.spin(reverse, (Controller1.Axis1.value() + Controller1.Axis3.value()), percent);
    RFmotor.spin(reverse, (Controller1.Axis1.value() - Controller1.Axis3.value()), percent);
    RBmotor.spin(reverse, (Controller1.Axis1.value() - Controller1.Axis3.value()), percent);

    if (Controller1.ButtonLeft.pressing()){
      Launcher.spin(forward, 100, percent);
      wait(0.9, sec);
      Launcher.stop(hold);
    }

    if (Controller1.ButtonL1.pressing()) {
      LArm.spin(reverse, 100, percent);
      RArm.spin(forward, 100, percent);
      wait(0.4,sec);
    } 
  
    else if (Controller1.ButtonL2.pressing()) {
      LArm.spin(forward, 100, percent);
      RArm.spin(reverse, 100, percent);
      wait(0.4,sec);
    } 


    else if (Controller1.ButtonR1.pressing()){
      Intake.spin(reverse, 100, percent);
    }

    else if (Controller1.ButtonR2.pressing()){
      Intake.spin(forward, 100, percent);
    }

    if (Controller1.ButtonUp.pressing()){
      Launcher.spin(forward, 100, percent);
    }

    if (Controller1.ButtonDown.pressing()){
      Launcher.setPosition(0,degrees);
      Launcher.stop(hold);
    }
  
  
    else {
      // Stop the arms only if neither ButtonL2 nor ButtonL1 is pressed
      LArm.stop(hold);
      RArm.stop(hold);
      


    wait(20, msec); // Sleep the task for a short amount of time to
                    // prevent wasted resources.
  }

    wait(20, msec); // Sleep the task for a short amount of time to
                    // prevent wasted resources.
  }
}

//
// Main will set up the competition functions and callbacks.
//
int main() {
  // Set up callbacks for autonomous and driver control periods.
  Competition.autonomous(autonomous);
  Competition.drivercontrol(usercontrol);

  // Run the pre-autonomous function.
  pre_auton();

  // Prevent main from exiting with an infinite loop.
  while (true) {
    wait(100, msec);
  }
}
