function validateForm() {
	let x = document.forms["myForm"]["fname"].value;
	if (x == "") {
	alert("Name must not be empty");
	return false;
	}
}