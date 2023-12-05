//var nom = prompt("Entrez votre nom");
//alert('Salut'nom'sympa de te voir');
//var prénom = prompt("Entrez votre prénom");
//var sexe = prompt("Entrez votre sexe");
//var poids = prompt("Entrez votre poids");

var createtextbox = document.createElement("INPUT");
createtextbox.setAttribute("type", "text");

function showData (form) {
    var dataRcv = form.inputbox.value;
    alert ("Vos informations: " + dataRcv);
}
var showData = document.getElementById("myForm").elements[1].value;

function setData (form) {
    form.inputbox.value = "Value to be set!"
}
