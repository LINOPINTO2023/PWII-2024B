let lienzo = document.getElementById('canvas');
let contexto = lienzo.getContext('2d');

// opciones de palabras para el juego
let listaPalabras = ["PROGRAMACION", "CANVAS", "JAVASCRIPT", "INGENIERIA", "DUTIC", "SISTEMAS"];

// contadores y variables
let palabraSecreta;
let aciertos;
let fallos;
let maxFallos = 6;
let cantidadErrores = 0;

// funcion que inicia el juego
function comenzarJuego() {
    palabraSecreta = listaPalabras[Math.floor(Math.random() * listaPalabras.length)].toUpperCase();  // palabra aleatoria
    aciertos = Array(palabraSecreta.length).fill("_");
    fallos = [];
    cantidadErrores = 0;
    contexto.clearRect(0, 0, lienzo.width, lienzo.height);  // limpia el canvas.
    dibujarHorca();  // volver a dibujar la horca
    mostrarPalabra();
    mostrarFallos();
    document.getElementById('resultado').innerHTML = '';  // limpia el mensaje de resultado
    document.getElementById('reiniciarBtn').style.display = 'none';  // oculta el botón de reinicio
    document.getElementById('letraInput').disabled = false;  // habilita la entrada de letras
}

// Dibuja la horca en el canvas
function dibujarHorca() {
    contexto.lineWidth = 2;
    contexto.beginPath();

    // base
    contexto.moveTo(50, 180);
    contexto.lineTo(150, 180);

    // poste
    contexto.moveTo(100, 180);
    contexto.lineTo(100, 50);

    // travesaño
    contexto.moveTo(100, 50);
    contexto.lineTo(150, 50);

    // soga
    contexto.moveTo(150, 50);
    contexto.lineTo(150, 70);

    contexto.stroke();
}

// dibuja las partes del ahorcado en el canvas segun vaya el juego
function dibujarAhorcado(paso) {
    contexto.lineWidth = 2;

    switch (paso) {
        case 1:
            // cabeza
            contexto.beginPath();
            contexto.arc(150, 80, 10, 0, Math.PI * 2, true);
            contexto.stroke();
            break;
        case 2:
            // cuerpo
            contexto.moveTo(150, 90);
            contexto.lineTo(150, 130);
            contexto.stroke();
            break;
        case 3:
            // braz-1
            contexto.moveTo(150, 100);
            contexto.lineTo(130, 110);
            contexto.stroke();
            break;
        case 4:
            // braz-2
            contexto.moveTo(150, 100);
            contexto.lineTo(170, 110);
            contexto.stroke();
            break;
        case 5:
            // pierna-1
            contexto.moveTo(150, 130);
            contexto.lineTo(130, 160);
            contexto.stroke();
            break;
        case 6:
            // pierna-2
            contexto.moveTo(150, 130);
            contexto.lineTo(170, 160);
            contexto.stroke();
            break;
        default:
            console.log("Juego terminado.");
    }
}

// muestra la palabra oculta obtenida del array de palabras
function mostrarPalabra() {
    document.getElementById('palabra').innerHTML = aciertos.join(" ");
}

// muestra las letras incorrectas que el jugador haya puesto
function mostrarFallos() {
    document.getElementById('letrasIncorrectas').innerHTML = "Letras incorrectas: " + fallos.join(", ");
}

// Verifica si la letra es o no es correcta
function comprobarLetra(letra) {
    if (palabraSecreta.includes(letra)) {
        for (let i = 0; i < palabraSecreta.length; i++) {
            if (palabraSecreta[i] === letra) {
                aciertos[i] = letra;
            }
        }
    } else {
        if (!fallos.includes(letra)) {
            fallos.push(letra);
            cantidadErrores++;
            dibujarAhorcado(cantidadErrores);
        }
    }
    mostrarPalabra();
    mostrarFallos();
    revisarEstadoJuego();
}

// da al boton la funcion de comprobar
document.getElementById('adivinarBtn').onclick = function() {
    let letraIngresada = document.getElementById('letraInput').value.toUpperCase();
    document.getElementById('letraInput').value = "";
    if (letraIngresada && letraIngresada.length === 1 && /^[A-ZÑ]$/.test(letraIngresada)) {
        comprobarLetra(letraIngresada);
    } else {
        alert("Por favor, ingresa una letra válida.");
    }
}

// funcion para el reinicio del jujego 
document.getElementById('reiniciarBtn').onclick = function() {
    comenzarJuego();  // restart
}

// funcion para manejar el cambio del menu al juego
document.getElementById('startBtn').onclick = function() {
    document.getElementById('menu').style.display = 'none';
    document.getElementById('game').style.display = 'block';
    comenzarJuego();  // start
}
