window.onload = initAll;

function initAll() {
	let ans = prompt("How many prime numbers to display?","10");
	try {
		if (!ans || isNaN(ans) || ans <= 0 || Math.round(ans) != ans) {
			throw new Error("Not a valid number");
		}
		calculatePrimesArray(ans);
	}
	catch (errMsg) {
		alert(errMsg.message);
	}
}

function calculatePrimesArray(numberOfPrimes) {
	// array for primes, your code goes below
	let primes = [];

	// add 2 to prime array, 'if' test
	if (numberOfPrimes >= 1) {
		// enter your code here
		primes.push(2);
	}
	
	let lastTested = 2;
	// loop while array needs primes added
	while ( primes.length < numberOfPrimes ) {
		// increment tested number
		lastTested++;
		
		// pass to function to test
		const isPrime = testForPrime(lastTested, primes);
		
		// if prime add to array
		if (isPrime) {
			// enter your code below this line
			primes.push(lastTested);
		}
	}
		
	displayPrimes(numberOfPrimes, primes);
}

function testForPrime(numberToTest, primes) {
	let upperLimit = Math.ceil(Math.sqrt(numberToTest));
	
	// loop until prime divisor is greater than upper limit to test
	// compare the current item in the array against the upperLimit
	for (let i = 0; i < upperLimit ; i++) {
		// check to see if the numberToTest can be evenly divided
		// by the current prime, check for the remainder
		// What should that remainder be?
		if ( numberToTest % primes[i] === 0 ) {
			return false;
		}
	}
	// after loop number must be prime
	// any number that can't be evenly divided by one of the primes
	// must be a prime so return true
	return true;
}

function displayPrimes(numberOfPrimes, primes) {
	document.write("You wanted this many primes: " + 
		numberOfPrimes + "<br/>");

	let primeString = "";
	for (let i = 0; i < primes.length - 1; i++) {
		primeString += primes[i] + ", ";
	}
	primeString += primes[primes.length - 1];
	
	// add primes to end of display text
	document.write("The first " + numberOfPrimes + 
		" prime numbers are: " + primeString);
}

