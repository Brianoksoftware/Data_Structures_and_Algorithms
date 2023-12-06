//Factorial finder ES6
n = 4
const factorial = (n) => {
	if(n < 0){
		console.log("ERROR. Enter non-negative number!");
	}

	else if(n < 2){
		return 1;
	}

	else{
		return n * factorial(n - 1);
	}
}

console.log("Factorial of " + n + " is: ", factorial(n));


//Another factorial example using recursion
n = 4;
const find_factorial = (n) => {
	if(n < 0){
		console.log("Enter positive number!");
	}
	else if(n < 2){
		return 1;
	}
	else{
		return n * find_factorial(n - 1);
	}
}
console.log("Factorial of " + n + " is:", find_factorial(n))
