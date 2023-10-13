window.onload = initAll;

function initAll() {

	var ans = prompt("Enter a positive number", "");
	try {
		if (!ans || isNaN(ans) || ans < 0) {
			throw new Error("Not a valid number");
		}
		let sqrt = Math.sqrt(ans);
		let message = "The square root of " + ans + " is " + sqrt;
		alert(message);
		document.write(message);
	}
	catch (errMsg) {
		alert(errMsg.message);
	}
}