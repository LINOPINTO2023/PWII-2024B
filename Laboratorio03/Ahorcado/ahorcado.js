let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');

// Lista de palabras
let palabras = ["JAVASCRIPT", "PROGRAMACION", "DESARROLLO", "FRONTEND", "BACKEND", "ALGORITMO", "INTERFAZ", "FUNCION", "OBJETO", "VARIABLE"];

// Variables de juego
let palabra;
let letrasCorrectas;
let letrasIncorrectas;
let maxErrores = 6;
let errores = 0;

// Función para iniciar el juego
function iniciarJuego() {
    palabra = palabras[Math.floor(Math.random() * palabras.length)].toUpperCase();  // Selecciona una palabra aleatoria
    letrasCorrectas = Array(palabra.length).fill("_");
    letrasIncorrectas = [];
    errores = 0;
    ctx.clearRect(0, 0, canvas.width, canvas.height);  // Limpiar el canvas completamente
    drawGallows();  // Redibujar la horca vacía
    mostrarPalabra();
    mostrarLetrasIncorrectas();
    document.getElementById('resultado').innerHTML = '';  // Limpia el mensaje de resultado
    document.getElementById('reiniciarBtn').style.display = 'none';  // Oculta el botón de reinicio
    document.getElementById('letraInput').disabled = false;  // Habilitar la entrada de letras
}

// Dibujar la horca vacía
function drawGallows() {
    ctx.lineWidth = 2;
    ctx.beginPath();

    // Base de la horca
    ctx.moveTo(50, 180);
    ctx.lineTo(150, 180);

    // Poste vertical
    ctx.moveTo(100, 180);
    ctx.lineTo(100, 50);

    // Poste horizontal
    ctx.moveTo(100, 50);
    ctx.lineTo(150, 50);

    // Cuerda
    ctx.moveTo(150, 50);
    ctx.lineTo(150, 70);

    ctx.stroke();
}

// Dibujar las diferentes partes del cuerpo paso a paso
function drawHangman(step) {
    ctx.lineWidth = 2;

    switch (step) {
        case 1:
            // Cabeza
            ctx.beginPath();
            ctx.arc(150, 80, 10, 0, Math.PI * 2, true);
            ctx.stroke();
            break;
        case 2:
            // Cuerpo
            ctx.moveTo(150, 90);
            ctx.lineTo(150, 130);
            ctx.stroke();
            break;
        case 3:
            // Brazo izquierdo
            ctx.moveTo(150, 100);
            ctx.lineTo(130, 110);
            ctx.stroke();
            break;
        case 4:
            // Brazo derecho
            ctx.moveTo(150, 100);
            ctx.lineTo(170, 110);
            ctx.stroke();
            break;
        case 5:
            // Pierna izquierda
            ctx.moveTo(150, 130);
            ctx.lineTo(130, 160);
            ctx.stroke();
            break;
        case 6:
            // Pierna derecha
            ctx.moveTo(150, 130);
            ctx.lineTo(170, 160);
            ctx.stroke();
            break;
        default:
            console.log("Juego terminado.");
    }
}

// Mostrar la palabra oculta
function mostrarPalabra() {
    document.getElementById('palabra').innerHTML = letrasCorrectas.join(" ");
}

// Actualizar letras incorrectas
function mostrarLetrasIncorrectas() {
    document.getElementById('letrasIncorrectas').innerHTML = "Letras incorrectas: " + letrasIncorrectas.join(", ");
}

// Verificar si la letra es correcta o incorrecta
function verificarLetra(letra) {
    if (palabra.includes(letra)) {
        for (let i = 0; i < palabra.length; i++) {
            if (palabra[i] === letra) {
                letrasCorrectas[i] = letra;
            }
        }
    } else {
        if (!letrasIncorrectas.includes(letra)) {
            letrasIncorrectas.push(letra);
            errores++;
            drawHangman(errores);
        }
    }
    mostrarPalabra();
    mostrarLetrasIncorrectas();
    verificarEstadoJuego();
}

// Verificar si el jugador ha ganado o perdido
function verificarEstadoJuego() {
    if (!letrasCorrectas.includes("_")) {
        document.getElementById('resultado').innerHTML = "¡Felicidades! Ganaste. La palabra era: " + palabra;
        document.getElementById('reiniciarBtn').style.display = 'block';  // Mostrar botón de reinicio
        document.getElementById('letraInput').disabled = true;  // Deshabilitar la entrada de letras
    } else if (errores >= maxErrores) {
        document.getElementById('resultado').innerHTML = "Lo siento, perdiste. La palabra era: " + palabra;
        document.getElementById('reiniciarBtn').style.display = 'block';  // Mostrar botón de reinicio
        document.getElementById('letraInput').disabled = true;  // Deshabilitar la entrada de letras
    }
}

// Manejo del botón para adivinar letra
document.getElementById('adivinarBtn').onclick = function() {
    let letra = document.getElementById('letraInput').value.toUpperCase();
    document.getElementById('letraInput').value = "";
    if (letra && letra.length === 1 && /^[A-ZÑ]$/.test(letra)) {
        verificarLetra(letra);
    } else {
        alert("Por favor, ingresa una letra válida.");
    }
}

// Manejo del botón de reinicio
document.getElementById('reiniciarBtn').onclick = function() {
    iniciarJuego();  // Reiniciar el juego
}

// Manejo del botón de inicio (Start)
document.getElementById('startBtn').onclick = function() {
    document.getElementById('menu').style.display = 'none';
    document.getElementById('game').style.display = 'block';
    iniciarJuego();  // Iniciar el juego por primera vez
}
