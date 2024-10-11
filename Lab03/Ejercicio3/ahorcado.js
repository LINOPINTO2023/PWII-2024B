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

// Inicialización del juego
inicializarJuego();
   
// Función para inicializar o reiniciar el juego
function inicializarJuego() {
        palabra = palabrasSimples[Math.floor(Math.random() * palabrasSimples.length)];
        palabraArray = palabra.split(''); //USO DE SPLIT PARA CONVERTIR EN UN ARRAY DE CHARS
        palabraOculta = Array(palabra.length).fill('_');/*Se crea un nuevo array vacío con la misma longitud que la palabra seleccionada. 
            Luego, fill('_') llena ese array con guiones bajos (_)*/
        errores = 0;
        // Limpiar el canvas completamente y reiniciar el contexto
            ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpiar todo el canvas
            ctx.beginPath(); // Reiniciar el camino de dibujo (muy importante)

        // Limpiar el mensaje final
            mensajeFinal.textContent = '';
            mensajeFinal.style.display = 'none'; // Ocultar el cuadro del mensaje al reiniciar

        // Dibujar la base y el poste al inicio
            dibujarBaseYPoste();

        // Mostrar la palabra oculta
            palabraHTML.textContent = palabraOculta.join(' ');

        // Limpiar el teclado
        teclado.innerHTML = '';
        //Crear un botón para cada letra del alfabeto y agregarlo al teclado.
            const letras = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'.split('');
            letras.forEach(letra => {
                const botonLetra = document.createElement('div');//Se crea un nuevo elemento <div> que representará un botón para la letra actual
                botonLetra.textContent = letra; //Se establece el contenido de texto del botón como la letra actual
                botonLetra.classList.add('tecla'); //Se añade la clase CSS tecla al botón
                botonLetra.addEventListener('click', () => manejarLetra(letra, botonLetra)); //evento de clic al botón
                teclado.appendChild(botonLetra); //el botón creado se agrega al elemento teclado
            });

        // Ocultar el botón "Volver a Jugar"
            botonReiniciar.style.display = 'none';
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
// Función para manejar la letra seleccionada
    function manejarLetra(letra, boton) {
        boton.classList.add('disabled'); // Desactivar la tecla
        if (palabraArray.includes(letra)) { //Comprobar si el array palabraArray incluye la letra que el jugador acaba de adivinar.
            // La letra es correcta, actualizar la palabra oculta
                palabraArray.forEach((letraPalabra, index) => {
                    if (letraPalabra === letra) {
                        palabraOculta[index] = letra;
                    }
                });
                palabraHTML.textContent = palabraOculta.join(' '); //muestra la palabra oculta actualizada en el HTML.

            // Verificar si se ha ganado
                if (palabraOculta.join('') === palabra) {
                    mostrarMensajeFinal('¡Felicidades! Has ganado.', true);
                }
        } else {
            // La letra es incorrecta, agregar error
                errores++;
                dibujarAhorcado(errores);
        }
    }
// Función para mostrar el botón "Volver a Jugar"
    function mostrarBotonReiniciar() {
        botonReiniciar.style.display = 'inline-block';
    }
// Función para desactivar todo el teclado
    function desactivarTeclado() {
        const teclas = document.querySelectorAll('.tecla'); //seleccionar todos los elementos  que tienen la clase CSS .tecla
        teclas.forEach(tecla => tecla.classList.add('disabled')); //agrega la clase disabled a su lista de clases
    }
// Función para mostrar el mensaje final
    function mostrarMensajeFinal(mensaje, esVictoria) {
        mensajeFinal.textContent = mensaje;
        mensajeFinal.style.display = 'block'; // Mostrar el cuadro del mensaje
        desactivarTeclado(); // Desactivar todo el teclado
        mostrarBotonReiniciar(); // Mostrar el botón para volver a jugar
    }
// Función para reiniciar el juego cuando se hace clic en el botón
    function reiniciarJuego() {
        inicializarJuego();
    }

