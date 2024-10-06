const canvas = document.getElementById("Canvas");
const ctx = canvas.getContext("2d");

let listaPalabras = [
  "PROGRAMACION",
  "CANVAS",
  "HTML",
  "CSS",
  "JAVASCRIPT",
  "CHISTEMAS",
];
let palabraSecreta;
let letrasAdivinadas = [];
let intentosFallidos = 0;
const maxIntentos = 6;

function empezarJuego() {
  // Mostrar el canvas y los elementos del juego
  document.getElementById("Canvas").style.display = "block";
  document.getElementById("letraInput").style.display = "inline-block";
  document.getElementById("btnAdivinar").style.display = "inline-block";
  document.getElementById("img").style.display = "none";

  // Ocultar el botón "Empezar"
  document.getElementById("btnEmpezar").style.display = "none";

  // Inicializar el juego
  palabraSecreta =
    listaPalabras[
      Math.floor(Math.random() * listaPalabras.length)
    ].toLowerCase();
  letrasAdivinadas = Array(palabraSecreta.length).fill("_");
  document.getElementById("palabraGuiones").innerText =
    letrasAdivinadas.join(" ");

  dibujarEstructura();
}

function verificarLetra() {
  const input = document.getElementById("letraInput");
  const letra = input.value.toLowerCase();
  input.value = "";

  if (letra && letra.length === 1) {
    if (palabraSecreta.includes(letra)) {
      for (let i = 0; i < palabraSecreta.length; i++) {
        if (palabraSecreta[i] === letra) {
          letrasAdivinadas[i] = letra;
        }
      }
      document.getElementById("palabraGuiones").innerText =
        letrasAdivinadas.join(" ");

      if (!letrasAdivinadas.includes("_")) {
        document.getElementById("mensaje").innerText = "¡Ganaste!";
        document.getElementById("btnReiniciar").style.display = "inline-block";
        document.getElementById("letraInput").disabled = true;
        document.getElementById("btnAdivinar").disabled = true;
      }
    } else {
      intentosFallidos++;
      dibujarAhorcado(intentosFallidos);

      if (intentosFallidos === maxIntentos) {
        document.getElementById("mensaje").innerText =
          "¡Perdiste! La palabra era: " + palabraSecreta;
        document.getElementById("btnReiniciar").style.display = "inline-block";
        document.getElementById("letraInput").disabled = true;
        document.getElementById("btnAdivinar").disabled = true;
      }
    }
  }
}

function dibujarEstructura() {
  // Dibujar la base
  ctx.beginPath();
  ctx.moveTo(50, 380);
  ctx.lineTo(250, 380);
  ctx.stroke();

  // Dibujar el poste
  ctx.beginPath();
  ctx.moveTo(100, 380);
  ctx.lineTo(100, 50);
  ctx.lineTo(200, 50);
  ctx.lineTo(200, 100);
  ctx.stroke();
}

function dibujarAhorcado(paso) {
  switch (paso) {
    case 1: // Cabeza
      ctx.beginPath();
      ctx.arc(200, 130, 30, 0, Math.PI * 2);
      ctx.stroke();
      break;
    case 2: // Torso
      ctx.beginPath();
      ctx.moveTo(200, 160);
      ctx.lineTo(200, 250);
      ctx.stroke();
      break;
    case 3: // Brazo izquierdo
      ctx.beginPath();
      ctx.moveTo(200, 180);
      ctx.lineTo(170, 220);
      ctx.stroke();
      break;
    case 4: // Brazo derecho
      ctx.beginPath();
      ctx.moveTo(200, 180);
      ctx.lineTo(230, 220);
      ctx.stroke();
      break;
    case 5: // Pierna izquierda
      ctx.beginPath();
      ctx.moveTo(200, 250);
      ctx.lineTo(170, 300);
      ctx.stroke();
      break;
    case 6: // Pierna derecha
      ctx.beginPath();
      ctx.moveTo(200, 250);
      ctx.lineTo(230, 300);
      ctx.stroke();
      break;
  }
}

function reiniciarJuego() {
  intentosFallidos = 0;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  document.getElementById("mensaje").innerText = "";
  document.getElementById("btnReiniciar").style.display = "none";
  document.getElementById("letraInput").disabled = false;
  document.getElementById("btnAdivinar").disabled = false;

  // Redibujar la estructura del ahorcado
  dibujarEstructura();

  empezarJuego();
}

iniciarJuego();
