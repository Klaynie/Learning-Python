/* Create a factory function named robotFactory that has two parameters model and mobile. Make the function return an object.
In the object, add a key of model with the value of the model parameter. Add another property that has a key of mobile with a
value of the mobile parameter. 

Then add a method named beep without a parameter that will log 'Beep Boop' to the console.
*/

const robotFactory = (model, mobile) =>
{
  return {
    model: model,
    mobile: mobile,
    beep() {
      console.log('Beep Boop');
    }
  }
};

/* Use your factory function by declaring a const variable named tinCan. Assign to tinCan the value of calling robotFactory
with the first argument of 'P-500' and the second argument of true. */

const tinCan = robotFactory('P-500', true);

tinCan.beep();

/* Shorthand Notation */

const robotFactoryShort = (model, mobile) =>
{
  return {
    model,
    mobile,
    beep() {
      console.log('Balala');
    }
  }
};

const baymax = robotFactoryShort('Big Hero 6', true);

baymax.beep();