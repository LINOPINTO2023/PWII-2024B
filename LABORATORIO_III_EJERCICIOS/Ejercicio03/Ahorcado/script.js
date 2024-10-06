const palabras = ["JAVASCRIPT", "HTML", "CSS", "AHORCADO", "CODIGO"];
let palabraSeleccionada = '';
let letrasAdivinadas = [];
let intentos = 6;
let juegoTerminado = false;

const canvas = document.getElementById('ahorcadoCanvas');
const ctx = canvas.getContext('2d');

function iniciarJuego() {
    palabraSeleccionada = palabras[Math.floor(Math.random() * palabras.length)];
    letrasAdivinadas = Array(palabraSeleccionada.length).fill('_');
    intentos = 6;
    juegoTerminado = false;
    document.getElementById('message').textContent = '';
    mostrarPalabra();
    dibujarAhorcado();
    generarTeclado();
}

function mostrarPalabra() {
    document.getElementById('wordContainer').textContent = letrasAdivinadas.join(' ');
}

function generarTeclado() {
    const teclado = document.getElementById('keyboard');
    teclado.innerHTML = '';
    const letras = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ';

    for (let letra of letras) {
        const button = document.createElement('button');
        button.textContent = letra;
        button.onclick = () => manejarLetra(letra);
        teclado.appendChild(button);
    }
}

function manejarLetra(letra) {
    if (juegoTerminado) return;

    let acierto = false;
    for (let i = 0; i < palabraSeleccionada.length; i++) {
        if (palabraSeleccionada[i] === letra) {
            letrasAdivinadas[i] = letra;
            acierto = true;
        }
    }

    if (!acierto) {
        intentos--;
        dibujarAhorcado();
    }

    mostrarPalabra();
    verificarEstadoJuego();
}

function verificarEstadoJuego() {
    if (letrasAdivinadas.join('') === palabraSeleccionada) {
        document.getElementById('message').textContent = '¡Ganaste!';
        juegoTerminado = true;
    } else if (intentos === 0) {
        document.getElementById('message').textContent = 'Perdiste. La palabra era ' + palabraSeleccionada;
        juegoTerminado = true;
    }
}

function dibujarAhorcado() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.lineWidth = 4;
    ctx.strokeStyle = '#333';
    ctx.beginPath();
    ctx.moveTo(10, 140);
    ctx.lineTo(140, 140);
    ctx.moveTo(40, 140);
    ctx.lineTo(40, 20);  
    ctx.lineTo(100, 20); 
    ctx.lineTo(100, 40); 
    ctx.stroke();

    if (intentos <= 5) {
        ctx.beginPath();
        ctx.arc(100, 50, 10, 0, Math.PI * 2);
        ctx.stroke();
    }
    if (intentos <= 4) {
        ctx.moveTo(100, 60);
        ctx.lineTo(100, 100);
        ctx.stroke();
    }
    if (intentos <= 3) {
        ctx.moveTo(100, 70);
        ctx.lineTo(80, 90);
        ctx.stroke();
    }
    if (intentos <= 2) {
        ctx.moveTo(100, 70);
        ctx.lineTo(120, 90);
        ctx.stroke();
    }
    if (intentos <= 1) {
        ctx.moveTo(100, 100);
        ctx.lineTo(80, 120);
        ctx.stroke();
    }
    if (intentos <= 0) {
        ctx.moveTo(100, 100);
        ctx.lineTo(120, 120);
        ctx.stroke();
    }
}

function resetGame() {
    iniciarJuego();
}

window.onload = iniciarJuego;
