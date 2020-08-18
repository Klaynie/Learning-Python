function factorial(int) {
    if (int === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

function iterative_factorial(int) {
    let result = 1;
    for (i = 1; i <= int; i++) {
        result *= i;
    }
    return result;
}

console.log(factorial(6));
console.log(iterative_factorial(6));