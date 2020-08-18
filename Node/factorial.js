function factorial(int) {
    if (int === 0) {
        return 1;
    } else {
        recurse = factorial(int - 1);
        result = int * recurse;
        return result;
    }
}

console.log(factorial(6));