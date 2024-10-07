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
}
