var contactForm = document.getElementById("contact");
contactForm.addEventListener("submit", function(event) {

	var contactDiv = document.getElementById("result");
	contactDiv.innerHTML = localStorage.curlocation;

	contactDiv.classList.remove("error");
	contactDiv.classList.remove("send");

	event.preventDefault();

	var firstname = document.getElementById("firstname").value; 
	var lastname = document.getElementById("lastname").value;
	var subject = document.getElementById("subject").value;
	var message = document.getElementById("message").value;

	contactDiv.innerHTML = "Error: Some field need to be filled; ";
	if (firstname.length == 0){
		contactDiv.innerHTML += " First name";
	} 
	if (lastname.length == 0) {
		contactDiv.innerHTML += "  Last name ";
	} 
	if (subject.length == 0) {
		contactDiv.innerHTML += "  Subject ";
	} 
	if (message.length == 0) {
		contactDiv.innerHTML += "  Message ";
	} 
	else{
		contactDiv.innerHTML = "Your Message has been sent successfully";
	}
	if (contactDiv.innerHTML != "Your Message has been sent successfully") {
		contactDiv.classList.add("send");
	} else {
		contactDiv.classList.add("error");
	}

})