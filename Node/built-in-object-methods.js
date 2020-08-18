const robot = {
	model: 'SAL-1000',
  mobile: true,
  sentient: false,
  armor: 'Steel-plated',
  energyLevel: 75
};

/* The Object.keys() method returns an array of a given object's own enumerable property names,
iterated in the same order that a normal loop would.*/
const robotKeys = Object.keys(robot);

console.log(robotKeys);

// Declare robotEntries below this line:
const robotEntries = Object.entries(robot);

console.log(robotEntries);

/* Declare a const variable named newRobot. newRobot will be a new object that has all the
properties of robot and the properties in the following object:
{laserBlaster: true, voiceRecognition: true}. Make sure that you are not changing the robot object!*/
const newRobot = Object.assign({laserBlaster: true, voiceRecognition: true}, robot);

console.log(newRobot);