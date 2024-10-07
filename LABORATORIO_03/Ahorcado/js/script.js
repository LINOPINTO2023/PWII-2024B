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
    if (!letra || !/^[A-ZÑ]$/.test(letra)) {
        alert("Introduce una letra válida");
        return;
    }

    if (palabra.includes(letra)) {
        let nuevaPalabraAdivinada = '';
        for (let i = 0; i < palabra.length; i++) {
            if (palabra[i] === letra) {
                nuevaPalabraAdivinada += letra;
            } else {
                nuevaPalabraAdivinada += palabraAdivinada[i];
            }
        }
        palabraAdivinada = nuevaPalabraAdivinada;
        document.getElementById('palabra').textContent = palabraAdivinada;
    } else {
        intentos++;
        dibujarAhorcado(intentos);
    }
    
function dibujarAhorcado(intentos) {
    const cuadro = document.getElementById('cuadro');
    const dibujar = cuadro.getContext('2d');

    if (intentos === 1) {
        dibujar.beginPath();
        dibujar.moveTo(50, 350);
        dibujar.lineTo(150, 350);
        dibujar.stroke();
    } else if (intentos === 2) {
        dibujar.beginPath();
        dibujar.moveTo(100, 350);
        dibujar.lineTo(100, 50);
        dibujar.stroke();
    } else if (intentos === 3) {
        dibujar.beginPath();
        dibujar.moveTo(100, 50);
        dibujar.lineTo(250, 50);
        dibujar.stroke();
    } else if (intentos === 4) {
        dibujar.beginPath();
        dibujar.moveTo(250, 50);
        dibujar.lineTo(250, 100);
        dibujar.stroke();
    } else if (intentos === 5) {
        dibujar.beginPath();
        dibujar.arc(250, 130, 30, 0, Math.PI * 2);
        dibujar.stroke();
    } else if (intentos === 6) {
        dibujar.beginPath();
        dibujar.moveTo(250, 160);
        dibujar.lineTo(250, 250);
        dibujar.stroke();
    } else if (intentos === 7) {
        dibujar.beginPath();
        dibujar.moveTo(250, 200);
        dibujar.lineTo(220, 180);
        dibujar.stroke();
    } else if (intentos === 8) {
        dibujar.beginPath();
        dibujar.moveTo(250, 200);
        dibujar.lineTo(280, 180);
        dibujar.stroke();
    } else if (intentos === 9) {
        dibujar.beginPath();
        dibujar.moveTo(250, 250);
        dibujar.lineTo(220, 300);
        dibujar.stroke();
    } else if (intentos === 10) {
        dibujar.beginPath();
        dibujar.moveTo(250, 250);
        dibujar.lineTo(280, 300);
        dibujar.stroke();
    }
}

}
