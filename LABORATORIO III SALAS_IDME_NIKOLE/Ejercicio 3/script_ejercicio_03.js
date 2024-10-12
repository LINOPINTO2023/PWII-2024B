const palabras = ['programacion', 'javascript', 'ahorcado', 'tecnologia'];
let palabraSeleccionada = '';
let palabraAdivinada = [];
let intentosIncorrectos = 0;
const maxIntentos = 6;

const lienzo = document.getElementById('lienzoAhorcado');
const contexto = lienzo.getContext('2d');
const mostrarPalabra = document.getElementById('mostrarPalabra');
const inputLetra = document.getElementById('inputLetra');
const btnAdivinar = document.getElementById('btnAdivinar');
const btnReiniciar = document.getElementById('btnReiniciar');
const mensaje = document.getElementById('mensaje');
function iniciarJuego() {
    palabraSeleccionada = palabras[Math.floor(Math.random() * palabras.length)];
    palabraAdivinada = Array(palabraSeleccionada.length).fill('_');
    intentosIncorrectos = 0;
    actualizarPalabra();
    limpiarLienzo();
    mensaje.textContent = '';
    btnAdivinar.disabled = false;
  }
  function actualizarPalabra() {
    mostrarPalabra.textContent = palabraAdivinada.join(' ');
  }
  function limpiarLienzo() {
    contexto.clearRect(0, 0, lienzo.width, lienzo.height);
  }
  function dibujarAhorcado() {
    contexto.strokeStyle = '#333';
    contexto.lineWidth = 2;
    switch (intentosIncorrectos) {
      case 1:
        // Base
        contexto.beginPath();
        contexto.moveTo(20, 230);
        contexto.lineTo(180, 230);
        contexto.stroke();
        break;
      case 2:
        // Poste vertical
        contexto.beginPath();
        contexto.moveTo(40, 230);
        contexto.lineTo(40, 20);
        contexto.stroke();
        break;
      case 3:
        // Poste horizontal
        contexto.beginPath();
        contexto.moveTo(40, 20);
        contexto.lineTo(100, 20);
        contexto.stroke();
        break;
      case 4:
        // Cuerda
        contexto.beginPath();
        contexto.moveTo(100, 20);
        contexto.lineTo(100, 50);
        contexto.stroke();
        break;
      case 5:
        // Cabeza
        contexto.beginPath();
        contexto.arc(100, 70, 20, 0, Math.PI * 2);
        contexto.stroke();
        break;
      case 6:
        // Cuerpo, brazos y piernas
        contexto.beginPath();
        contexto.moveTo(100, 90);
        contexto.lineTo(100, 150);
        contexto.moveTo(100, 110);
        contexto.lineTo(60, 100); // Brazo izquierdo
        contexto.moveTo(100, 110);
        contexto.lineTo(140, 100); // Brazo derecho
        contexto.moveTo(100, 150);
        contexto.lineTo(70, 190); // Pierna izquierda
        contexto.moveTo(100, 150);
        contexto.lineTo(130, 190); // Pierna derecha
        contexto.stroke();
        break;
    }
  }
  function hacerAdivinanza() {
    const letra = inputLetra.value.toLowerCase();
    if (letra.length !== 1 || !/[a-zñ]/.test(letra)) {
      mensaje.textContent = 'Por favor, ingresa una letra válida.';
      return;
    }
  
    if (palabraSeleccionada.includes(letra)) {
      for (let i = 0; i < palabraSeleccionada.length; i++) {
        if (palabraSeleccionada[i] === letra) {
          palabraAdivinada[i] = letra;
        }
      }
      actualizarPalabra();
      if (!palabraAdivinada.includes('_')) {
        mensaje.textContent = '¡Felicidades! Has ganado.';
        btnAdivinar.disabled = true;
      }
    } else {
      intentosIncorrectos++;
      dibujarAhorcado();
      if (intentosIncorrectos === maxIntentos) {
        mensaje.textContent = `Juego Terminado. La palabra era: ${palabraSeleccionada}`;
        btnAdivinar.disabled = true;
      }
    }
  
    inputLetra.value = '';
    inputLetra.focus();
  }