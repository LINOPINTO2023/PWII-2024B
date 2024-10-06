const buttons = document.querySelectorAll(".button");
const passwordField = document.getElementById("clave-internet");
const clearButton = document.getElementById("clear");

let numbers = Array.from({ length: 10 }, (_, i) => i);

numbers = numbers.sort(() => Math.random() - 0.5);

buttons.forEach((button, index) => {
    button.innerHTML = numbers[index];
});

buttons.forEach(button => {
    button.addEventListener('click', () => {
        if (button.textContent === "Limpiar") {
            passwordField.value = "";
        } else {
            passwordField.value += button.textContent;
        }
    });
});

clearButton.addEventListener('click', () => {
    passwordField.value = "";
});
