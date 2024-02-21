#include "vex.h"

using namespace vex;
using signature = vision::signature;
using code = vision::code;

// A global instance of brain used for printing to the V5 Brain screen
brain  Brain;

// VEXcode device constructors
controller Controller1 = controller(primary);
motor LFmotor = motor(PORT1, ratio18_1, false);
motor LBmotor = motor(PORT12, ratio18_1, false);
motor RFmotor = motor(PORT10, ratio18_1, false);
motor RBmotor = motor(PORT19, ratio18_1, false);
motor LArm = motor(PORT11, ratio18_1, false);
motor RArm = motor(PORT20, ratio18_1, false);
motor Intake = motor(PORT8, ratio18_1, false);
motor Launcher = motor(PORT6, ratio18_1, false);
digital_in JumpA = digital_in(Brain.ThreeWirePort.A);

// VEXcode generated functions
// define variable for remote controller enable/disable
bool RemoteControlCodeEnabled = true;

/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Pro.
 * 
 * This should be called at the start of your int main function.
 */
void vexcodeInit( void ) {
  // nothing to initialize
}