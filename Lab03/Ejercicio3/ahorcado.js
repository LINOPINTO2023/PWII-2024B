// Variables 
let palabra;
let palabraArray;
let palabraOculta;
let errores;
const palabrasSimples = ["GATO", "PERRO", "CASA", "SOL", "LUNA", "AGUA"];
const canvas = document.getElementById('ahorcadoCanvas');
const ctx = canvas.getContext('2d'); /*LIENZO-DIBUJO*/
const palabraHTML = document.getElementById('palabra');
const teclado = document.getElementById('teclado');
const botonReiniciar = document.getElementById('botonReiniciar');
const mensajeFinal = document.getElementById('mensajeFinal');

// Función para inicializar o reiniciar el juego
function inicializarJuego() {
        palabra = palabrasSimples[Math.floor(Math.random() * palabrasSimples.length)];
        palabraArray = palabra.split(''); //USO DE SPLIT PARA CONVERTIR EN UN ARRAY DE CHARS
        palabraOculta = Array(palabra.length).fill('_');/*Se crea un nuevo array vacío con la misma longitud que la palabra seleccionada. 
            Luego, fill('_') llena ese array con guiones bajos (_)*/
        errores = 0;
}
// Función para dibujar la base y el poste (dibujados al inicio del juego)
    function dibujarBaseYPoste() {
        // Dibujar la base
        ctx.moveTo(10, 190);
        ctx.lineTo(100, 190);
        ctx.stroke();

        // Dibujar el poste vertical
        ctx.moveTo(55, 190);
        ctx.lineTo(55, 50);
        ctx.stroke();

        // Dibujar el brazo horizontal
        ctx.moveTo(55, 50);
        ctx.lineTo(120, 50);
        ctx.stroke();

        // Dibujar la cuerda
        ctx.moveTo(120, 50);
        ctx.lineTo(120, 80);
        ctx.stroke();
    }
// Función para dibujar las partes del ahorcado
    function dibujarAhorcado(errores) {
        ctx.beginPath(); // Reiniciar el camino de dibujo antes de cada nuevo trazo
        switch (errores) {
            case 1: // Dibujar la cabeza
                ctx.beginPath();
                ctx.arc(120, 90, 10, 0, Math.PI * 2);
                ctx.stroke();
                break;
            case 2: // Dibujar el cuerpo
                ctx.moveTo(120, 100);
                ctx.lineTo(120, 140);
                ctx.stroke();
                break;
            case 3: // Dibujar brazo izquierdo
                ctx.moveTo(120, 110);
                ctx.lineTo(100, 130);
                ctx.stroke();
                break;
            case 4: // Dibujar brazo derecho
                ctx.moveTo(120, 110);
                ctx.lineTo(140, 130);
                ctx.stroke();
                break;
            case 5: // Dibujar pierna izquierda
                ctx.moveTo(120, 140);
                ctx.lineTo(100, 170);
                ctx.stroke();
                break;
            case 6: // Dibujar pierna derecha (fin del juego)
                ctx.moveTo(120, 140);
                ctx.lineTo(140, 170);
                ctx.stroke();
                mostrarMensajeFinal(`¡Juego terminado! Has perdido. La palabra correcta era "${palabra}".`, false);
                break;
        }
    }