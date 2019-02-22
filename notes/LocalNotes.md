Local Notes

Good reference:
Code to control arm with PID for smooth motion, shows how to architect control loops, use C library with .ino file  -- https://github.com/lukicdarkoo/RobotArm

how to use a great library, tips on developing and using hte control board -- https://www.robotshop.com/community/robots/show/xyz-positioning-using-arduino-uno-for-6-dof-robotic-arm

A detailed and pedantic source with code and math -- https://www.circuitsathome.com/mcu/robotic-arm-inverse-kinematics-on-arduino/?utm_source=rb-community&utm_medium=robots&utm_campaign=xyz-positioning-using-arduino-uno-for-6-dof-robotic-arm

List of libraries (2dd0f - 6dof) -- https://www.xsimulator.net/community/faq/arduino-code-for-use-with-various-hardware-and-simtools.31/



Functions to make:
- keep hand parallel to world frame (table top)
- Move end of each finger to position(x,y,z)
- Smooth and simultaneous motion w/ PID
- Control loop that updates motion of arm every 50ms during move (PID)
- Cheeck if target is valid for arm to reach
- Limit motion to 1" less than max in all ranges
- Move .25" past target then come back to target
- Configurable 0 degree position for each motor
- Configurable lengths for each portion of arm (base to mid, mid to hand, hand to fingertips)
- Architecture - servo control, Arm control, PID
- function for each of desired poses (storage, pouring, waiting)
- Use mode for constant speed as well as PID, limit PID top speed, so you can develop with it in slow motion
- Add dancing?