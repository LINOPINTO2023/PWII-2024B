window.onload = function() {
    const buttons = document.querySelectorAll(".casilla");
    const numbers = Array.from({ length: 10 }, (_, i) => i).sort(() => Math.random() - 0.5);

    buttons.forEach((button, index) => {
        button.textContent = numbers[index];
        button.onclick = () => agregarNumero(numbers[index]); 
    });
};

function agregarNumero(numero) {
    const passwordField = document.getElementById("clave-internet");
    if (passwordField.value.length < 6) { 
        passwordField.value += numero; 
    }
}

function limpiarFormulario() {
    const passwordField = document.getElementById("clave-internet");
    passwordField.value = ""; 
}