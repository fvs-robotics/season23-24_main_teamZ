using namespace vex;

extern brain Brain;

// VEXcode devices
extern controller Controller1;
extern motor LFmotor;
extern motor LBmotor;
extern motor RFmotor;
extern motor RBmotor;
extern motor LArm;
extern motor RArm;
extern motor Intake;
extern motor Launcher;
extern digital_in JumpA;

/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Pro.
 * 
 * This should be called at the start of your int main function.
 */
void  vexcodeInit( void );