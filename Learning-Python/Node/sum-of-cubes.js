function sumOfCubes(array) {
    var result = 0;
    if (array.length != 0) {
        for(i = 0; i < array.length; i++) {
            result += Math.pow(array[i], 3);
        }
    }
    return result;
}

myArray = [4, 5, 9];
result = sumOfCubes(myArray);

console.log(result);