window.onload = getSecretNumber;
// Establish variables for secret, guess, valid_guess_count,
// and optionally a variable to represent a line break.
var lb = "<br />";
var secret;
var guess;
var valid_guess_count = 0;

function getSecretNumber() {
    // get a secret number
    // you may want to include a statement to show
    // the secret number while you are testing the program
    secret = Math.floor(Math.random() * 100) + 1;
    alert("Test hint. The secret number is: " + secret);
}

function checkGuess() {
    // This function should check whether a guess is a number.
    // It should compare the guess to the secret and 
    // report if the guess is correct, high, or low.
    // An advanced option would be to count the number of
    // valid guesses and display that for the user as well.
    // You can get the value typed in the text box by the user
    // with getElementByID function and the value property of the
    // returned element object.
    guess = document.getElementById('guess_input').value;
    if (isNaN(guess)) {
        document.getElementById('report').innerHTML = "That's not a number.";
    }
    if (guess == secret) {
        valid_guess_count += 1;
        document.getElementById('report').innerHTML = "You guessed it in " + valid_guess_count + " guesses!";

    } else if (guess < secret) {
        valid_guess_count += 1;
        document.getElementById('report').innerHTML = "Your guess is too LOW. Guess again.";
    } else if (guess > secret) {
        valid_guess_count += 1;
        document.getElementById('report').innerHTML = "Your guess is too HIGH. Guess again.";
    }
		
}
	
