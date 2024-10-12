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