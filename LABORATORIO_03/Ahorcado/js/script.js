const palabras = ["JAVASCRIPT", "PROGRAMACION", "CANVAS", "AHORCADO"];
let palabra = palabras[Math.floor(Math.random() * palabras.length)];
let palabraAdivinada = "_".repeat(palabra.length);
let intentos = 0;
const maxIntentos = 10;
let juegoTerminado = false;

document.getElementById('palabra').textContent = palabraAdivinada;



