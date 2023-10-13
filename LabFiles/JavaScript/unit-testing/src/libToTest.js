/* Functions to test */
function returnTrue() {
    console.log("returnTrue function entered ...");
    return true;
}
function principalPlusInterest(principal, interest) {
    console.log("The principalPlusInterest function entered ...");
    return principal * (1 + interest / 100);
}

let throwException = function () {
    console.log("The throwException function entered ...");
    throw new Error("User-defined exception thrown!");
}

module.exports = { 
    returnTrue,
    principalPlusInterest,
    throwException
  }