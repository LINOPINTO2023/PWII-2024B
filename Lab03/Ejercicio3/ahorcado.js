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
