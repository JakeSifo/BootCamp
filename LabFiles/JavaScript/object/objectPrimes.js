window.onload = function () {
	document.getElementById("tryPrimeDivisors").onclick = tryPrimeDivisorsMethod;
	document.getElementById("tryBruteForce").onclick = tryBruteForceMethod;
};

let numOfPrimesToTestFor = 300;

function tryPrimeDivisorsMethod() {
	console.log('calculating primes using divisor method')
	new DivisorsMethodPrimeCalculator(numOfPrimesToTestFor).run()
}

function tryBruteForceMethod() {
	console.log('calculating primes using brute-force method')
	new BruteForcePrimeCalculator(numOfPrimesToTestFor).run()
}

// COMPLETE - define the BruteForce constructor function
class PrimeCalculator {

	primes = [];
	numTests = 0;
	numPrimes = 0;

	constructor(numPrimes) { this.numPrimes = numPrimes }

	run() {
		this.calculatePrimesArray()
		this.displayResult()
	}

	calculatePrimesArray() {

		if (!this.testForPrime) {
			console.log('Skipping calc, testForPrime does not exist.');
			return;
		}
		if (this.numPrimes >= 1) {
			this.primes.push(2);
		}

		let lastTested = 2;
		// loop while array needs primes added
		while (this.primes.length < this.numPrimes) {
			// increment tested number
			lastTested++;

			// pass to function to test
			let isPrime = this.testForPrime(lastTested);

			// if prime add to array
			if (isPrime) {
				this.primes.push(lastTested);
			}
		}
	}

	// testForPrime(numberToTest) {
	// 	let upperLimit = Math.ceil(Math.sqrt(numberToTest));

	// 	// loop until prime divisor is greater than upper limit to test
	// 	for (let i = 0; this.primes[i] <= upperLimit; i++) {
	// 		this.numTests++;
	// 		if (numberToTest % this.primes[i] == 0) {
	// 			return false;
	// 		}
	// 	}
	// 	// after loop number must be prime
	// 	return true;
	// }

	displayResult() {
		const titleElement = document.getElementById("title")
		const numOfPrimesElement = document.getElementById("numberOfPrimes")
		const numTestsElement = document.getElementById("numTests")
		const primeStringElement = document.getElementById("primeString")

		titleElement.innerHTML = this.constructor.name
		numOfPrimesElement.innerHTML = "Number of primes: " + this.primes.length + "<br/>";
		numTestsElement.innerHTML = "The number of tests performed: " + this.numTests + "<br/>";
		primeStringElement.innerHTML = "The first " + this.primes.length + " prime numbers are: " + this.primes.join(', ');
	}
}


class DivisorsMethodPrimeCalculator extends PrimeCalculator {
	constructor(numPrimes) { super(numPrimes) }
	testForPrime(numberToTest) {
		// add code here
		let upperLimit = Math.ceil(Math.sqrt(numberToTest));

		// loop until prime divisor is greater than upper limit to test
		for (let i = 0; this.primes[i] <= upperLimit; i++) {
			this.numTests++;
			if (numberToTest % this.primes[i] == 0) {
				return false;
			}
		}
		// after loop number must be prime
		return true;
	}
}

class BruteForcePrimeCalculator extends PrimeCalculator {
	constructor(numPrimes) { super(numPrimes) }
	testForPrime(numberToTest) {
		// add code here
		let modval = Math.ceil(Math.sqrt(numberToTest))
		for (; modval > 1; modval--) {
			this.numTests++;
			if (numberToTest % modval == 0) {
				return false;
			}
		}
		return true;
	}
}
