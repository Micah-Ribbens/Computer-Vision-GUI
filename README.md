Finished Development: 02/27/2022
First two years of programming

# Summary
This was a GUI application that helped test the robot code through simulation. For robotics that year I wrote a vision
validation checker. We ran image processing code that would pick up the target that the robot shot at. It "saw" the target
because there was retro-reflective tape all around the target. Using the image processing, the software would know
how far away the robot was from the target and where it had to aim to shoot at the target. It did this by drawing a 
bounding box around all the retro-reflective objects and using some equations, the center of the box would give the 
distance from the target and where the robot had to aim.The image processing software was run on a raspberry pi 
and limelight. This meant that the entire shooting process could be automated (and mostly was automated). There was one
issue, however, other robot's lights would fool the image processing code into thinking that the robot light was a 
retro-reflective project. That is where my code came in. My code would get all the retro-reflective objects from the
image processing code. Then it would remove any extraneous objects that were not a part of the target. It did this by
choosing the plane (object's with x and y coordinates that are close to each other) with the most objects on it. This worked because the retro-reflective objects around the target were
all close to the same y coordinate. Therefore, if an object did not was not similar to any other object on a plane it would
create a new plane. While choosing the correct was not guaranteed, it was very unlikely that the wrong plane would be chosen.
Most of the extraneous retro-reflective objects were caused by a robot light, so there would be a plane of one.
