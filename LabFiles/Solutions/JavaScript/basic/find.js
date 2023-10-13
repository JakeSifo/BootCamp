window.onload = initAll;

function initAll() {
	document.getElementById("findById").onclick = findById;
	
}

function findById() {
	const id = document.getElementById("id_value").value;
	const e = document.getElementById(id);

	if (e != null) {
		e.style.backgroundColor = "yellow";
	} else {
		alert("Could not find element by ID: " + id);
	}

}

