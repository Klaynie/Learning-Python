const robot = {
    model : '1E78V2',
    energyLevel : 100,
    provideInfo() {
      return `I am ${this.model} and my current energy level is ${this.energyLevel}.`;
  }
};
  
console.log(robot.provideInfo());

const robot2 = {
    _model: '1E78V2',
    _energyLevel: 100,
    get energyLevel() {
    if (typeof(this._energyLevel) === 'number') {
        return `My current energy level is ${this._energyLevel}`;
    } else {
        return 'System malfunction: cannot retrieve energy level';
    }
  }
};  

console.log(robot2.energyLevel);