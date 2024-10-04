document.addEventListener("DOMContentLoaded", function () {
    const botones = document.querySelectorAll(".numeros4");

    // Generar un array de números del 0 al 9
    let numeros = Array.from({ length: 10 }, (_, i) => i);

    // Desordenar los números aleatoriamente
    numeros = numeros.sort(() => Math.random() - 0.5);

    // Asignar los números aleatorios a los botones
    botones.forEach((boton, index) => {
        boton.textContent = numeros[index];
    });
});
