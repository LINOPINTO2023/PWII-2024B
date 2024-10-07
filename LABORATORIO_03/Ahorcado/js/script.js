const palabras = ["JAVASCRIPT", "PROGRAMACION", "CANVAS", "AHORCADO"];
let palabra = palabras[Math.floor(Math.random() * palabras.length)];
let palabraAdivinada = "_".repeat(palabra.length);
let intentos = 0;
const maxIntentos = 10;
let juegoTerminado = false;

document.getElementById('palabra').textContent = palabraAdivinada;

function teclaPresionada(evento) {
    if (evento.key === 'Enter') {
        adivinarLetra();
    }
}

function adivinarLetra() {
    if (juegoTerminado) {
        return;
    }

    const inputLetra = document.getElementById('letra');
    const letra = inputLetra.value.toUpperCase();
    inputLetra.value = '';
}
