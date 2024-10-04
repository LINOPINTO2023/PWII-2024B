document.addEventListener("DOMContentLoaded", function () {
    const botones = document.querySelectorAll(".numeros4");
    const limpiarBtn = document.querySelector(".limpiar4");
    const inputClave = document.querySelector(".texto4_2 + div input");
    // Generar un array de números del 0 al 9
    let numeros = Array.from({ length: 10 }, (_, i) => i);

    // Desordenar los números aleatoriamente
    numeros = numeros.sort(() => Math.random() - 0.5);

    // Asignar los números aleatorios a los botones
    botones.forEach((boton, index) => {
        boton.textContent = numeros[index];
        // Añadir el evento de click a cada botón numérico
        boton.addEventListener("click", function () {
            // Agregar el número del botón al input de clave
            inputClave.value += boton.textContent;
        });        
    });
    // Limpiar el input cuando se presiona el botón "Limpiar"
    limpiarBtn.addEventListener("click", function () {
        inputClave.value = ''; // Borrar el contenido del input
    });    
});
