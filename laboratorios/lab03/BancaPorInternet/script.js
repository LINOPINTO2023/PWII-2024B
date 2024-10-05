document.addEventListener("DOMContentLoaded", () => {
    const teclado = document.getElementById("teclado");
    const input = document.getElementById("numeroDocumentoTeclado"); // Campo de texto para el teclado virtual
    const botonLimpiar = document.getElementById("boton-limpiar");

    const numeroDocumentoInput = document.getElementById("numeroDocumento"); // Campo de texto para el documento
    const tipoDocumentoInput = document.getElementById("tipoDocumento"); // Campo de selección del tipo de documento

    // Los números que tendrá el teclado
    const numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
    
    // Función para crear el teclado
    function crearTeclado() {
        teclado.innerHTML = ""; // Limpiar el teclado antes de regenerarlo

        // Aleatorizar el arreglo de números
        const numerosAleatorios = numeros.sort(() => Math.random() - 0.5);

        // Crear los botones para cada número en la cuadrícula
        for (let i = 0; i < numerosAleatorios.length; i++) {
            const boton = document.createElement("button");
            boton.textContent = numerosAleatorios[i];
            boton.onclick = () => ingresarNumero(numerosAleatorios[i]);
            teclado.appendChild(boton);
        }

        // Añadir el botón "Limpiar" al final (esto será fijo)
        const limpiarBtn = document.createElement("div");
        limpiarBtn.textContent = "Limpiar";
        limpiarBtn.onclick = limpiarEntrada;
        limpiarBtn.classList.add("btn-limpiar");
        teclado.appendChild(limpiarBtn);
    }

    // Ingresar número en el input
    function ingresarNumero(numero) {
        if (input.value.length < numeroDocumentoInput.maxLength) { // Limitar a la cantidad de dígitos según el tipo de documento
            input.value += numero;
        }
    }

    // Limpiar el campo de texto
    function limpiarEntrada() {
        input.value = "";
    }

    // Cambia el tamaño máximo del número de documento según el tipo de documento
    function actualizarCampo() {
        const tipoDocumento = tipoDocumentoInput.value;

        switch (tipoDocumento) {
            case "dni":
                numeroDocumentoInput.maxLength = 8;
                numeroDocumentoInput.placeholder = "DNI (8 dígitos)";
                break;
            case "ce":
                numeroDocumentoInput.maxLength = 12; 
                numeroDocumentoInput.placeholder = "Carnet de Extranjería (máximo 12 dígitos)";
                break;
            case "pasaporte":
                numeroDocumentoInput.maxLength = 9; 
                numeroDocumentoInput.placeholder = "Pasaporte (máximo 9 dígitos)";
                break;
            default:
                numeroDocumentoInput.maxLength = 0;
                numeroDocumentoInput.placeholder = "Seleccione un tipo de documento";
                break;
        }
    }

    // Ejecutar la función para crear el teclado
    crearTeclado();

    // Ejecutar la función de actualización cuando se cambia el tipo de documento
    tipoDocumentoInput.addEventListener("change", actualizarCampo);
});
