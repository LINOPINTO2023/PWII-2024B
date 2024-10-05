document.addEventListener("DOMContentLoaded", function () {
    const botones = document.querySelectorAll(".numeros4");
    const limpiarBtn = document.querySelector(".limpiar4");
    const inputClave = document.getElementById("area_clave");

    // Generar un array de números del 0 al 9
    let numeros = Array.from({ length: 10 }, (_, i) => i);

    // Desordenar los números aleatoriamente
    numeros = numeros.sort(() => Math.random() - 0.5);

    // Asignar los números aleatorios a los botones
    botones.forEach((boton, index) => {
        boton.textContent = numeros[index];
        // Añadir el evento de click a cada botón numérico
        boton.addEventListener("click", function () {
            // Limitar a 6 caracteres
            if (inputClave.value.length < 6) {
                inputClave.value += boton.textContent;
            }
        });
    });

    // Limpiar el input cuando se presiona el botón "Limpiar"
    limpiarBtn.addEventListener("click", function () {
        inputClave.value = ''; // Borrar el contenido del input
    });

    inputClave.addEventListener("input", function () {
        if (this.value.length > 6) {
            this.value = this.value.slice(0, 6);
        }
    });

    document.getElementById('changeButton').addEventListener('click', function () {
        const randomNumber = Math.floor(Math.random() * 6) + 1;
        
        const newSrc = `/imagenes/captcha/${randomNumber}.png`;
        document.getElementById('captchaImage').src = newSrc;
    });
});
