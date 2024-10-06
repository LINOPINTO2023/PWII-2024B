const canvas = document.getElementById("Canvas");
const ctx = canvas.getContext("2d");

const palabraSecreta = "Ahorcamela".toLowerCase();
let letrasAdivinadas = [];
let intentosFallidos = 0;
const maxIntentos = 6;

function iniciarJuego() {
  letrasAdivinadas = Array(palabraSecreta.length).fill("_");
  document.getElementById("palabraGuiones").innerText =
    letrasAdivinadas.join(" ");
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
      document.getElementById("palabraGuiones").innerText = letrasAdivinadas
        .join(" ")
        .replace(/\b\w/g, (c) => c.toUpperCase());

      if (!letrasAdivinadas.includes("_")) {
        document.getElementById("mensaje").innerText = "¡Ganaste!";
        document.querySelector("button").disabled = true;
      }
    } else {
      intentosFallidos++;
      dibujarAhorcado(intentosFallidos);

      if (intentosFallidos === maxIntentos) {
        document.getElementById("mensaje").innerText =
          "¡Perdiste! La palabra era: " +
          palabraSecreta.charAt(0).toUpperCase() +
          palabraSecreta.slice(1);
        document.querySelector("button").disabled = true;
      }
    }
  }
}

function dibujarAhorcado(paso) {
  switch (paso) {
    case 1:
      ctx.beginPath();
      ctx.moveTo(50, 380);
      ctx.lineTo(250, 380);
      ctx.stroke();
      break;
    case 2:
      ctx.beginPath();
      ctx.moveTo(100, 380);
      ctx.lineTo(100, 50);
      ctx.lineTo(200, 50);
      ctx.lineTo(200, 100);
      ctx.stroke();
      break;
    case 3:
      ctx.beginPath();
      ctx.arc(200, 130, 30, 0, Math.PI * 2);
      ctx.stroke();
      break;
    case 4:
      ctx.beginPath();
      ctx.moveTo(200, 160);
      ctx.lineTo(200, 250);
      ctx.stroke();
      break;
    case 5:
      ctx.beginPath();
      ctx.moveTo(200, 180);
      ctx.lineTo(170, 220);
      ctx.moveTo(200, 180);
      ctx.lineTo(230, 220);
      ctx.stroke();
      break;
    case 6:
      ctx.beginPath();
      ctx.moveTo(200, 250);
      ctx.lineTo(170, 300);
      ctx.moveTo(200, 250);
      ctx.lineTo(230, 300);
      ctx.stroke();
      break;
  }
}

iniciarJuego();
