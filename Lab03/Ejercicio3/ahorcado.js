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
