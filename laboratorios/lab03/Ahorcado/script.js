// Configuración del juego
const canvas = document.getElementById('hangmanCanvas');
const ctx = canvas.getContext('2d');

// Lista de palabras personalizable (puedes agregar las que quieras aquí)
const wordList = ["pantalla", "javascript", "ahorcado", "programacion", "desarrollador", "computadora"];
let wordToGuess = "";
let guessedLetters = [];
let wrongGuesses = 0;
const maxWrongGuesses = 6; // Número máximo de fallos
let wordDisplay = ""; // Palabra que se muestra al usuario

// Inicializar el juego con una palabra aleatoria de la lista
function initializeGame() {
    // Elegir una palabra aleatoria de la lista
    wordToGuess = wordList[Math.floor(Math.random() * wordList.length)];
    guessedLetters = [];
    wrongGuesses = 0;
    wordDisplay = "_ ".repeat(wordToGuess.length); // Inicializa con "_"
    document.getElementById('wordDisplay').textContent = `Palabra: ${wordDisplay}`;
    document.getElementById('message').textContent = '';
    document.getElementById('opportunities').textContent = `Oportunidades restantes: ${maxWrongGuesses}`;
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpiar el canvas
}

// Dibujar la figura del ahorcado
function drawHangman() {
    const steps = [
        () => ctx.arc(250, 100, 30, 0, Math.PI * 2), // Cabeza
        () => ctx.moveTo(250, 130), ctx.lineTo(250, 200), // Cuerpo
        () => ctx.moveTo(250, 150), ctx.lineTo(230, 180), // Brazo izquierdo
        () => ctx.moveTo(250, 150), ctx.lineTo(270, 180), // Brazo derecho
        () => ctx.moveTo(250, 200), ctx.lineTo(230, 240), // Pierna izquierda
        () => ctx.moveTo(250, 200), ctx.lineTo(270, 240) // Pierna derecha
    ];

    ctx.beginPath();
    ctx.lineWidth = 5;
    ctx.strokeStyle = "black";
    ctx.arc(250, 100, 30, 0, Math.PI * 2); // Dibuja la cabeza
    ctx.moveTo(250, 130); // Empieza a dibujar el cuerpo
    ctx.lineTo(250, 200); // Cuerpo
    ctx.moveTo(250, 150); 
    ctx.lineTo(230, 180); // Brazo izquierdo
    ctx.moveTo(250, 150);
    ctx.lineTo(270, 180); // Brazo derecho
    ctx.moveTo(250, 200);
    ctx.lineTo(230, 240); // Pierna izquierda
    ctx.moveTo(250, 200);
    ctx.lineTo(270, 240); // Pierna derecha
    ctx.stroke();
}

// Actualizar la visualización de la palabra en el DOM
function updateWordDisplay() {
    let display = wordToGuess.split('').map(letter => {
        if (guessedLetters.includes(letter)) {
            return letter;
        } else {
            return "_";
        }
    }).join(" ");

    document.getElementById('wordDisplay').textContent = `Palabra: ${display}`;
    wordDisplay = display;
}

// Comprobar si la letra adivinada es correcta
function guessLetter() {
    const inputElement = document.getElementById('letterInput');
    const letter = inputElement.value.toLowerCase();

    if (letter && !guessedLetters.includes(letter)) {
        guessedLetters.push(letter);
        inputElement.value = ""; // Limpiar el campo de entrada

        if (wordToGuess.includes(letter)) {
            updateWordDisplay();

            // Comprobar si ganó el jugador
            if (!wordDisplay.includes('_')) {
                document.getElementById('message').textContent = "¡Felicidades! Has adivinado la palabra!";
            }
        } else {
            // Aumentar el número de fallos
            wrongGuesses++;
            drawHangmanStep(wrongGuesses);

            // Comprobar cuántas oportunidades le quedan
            document.getElementById('opportunities').textContent = `Oportunidades restantes: ${maxWrongGuesses - wrongGuesses}`;

            // Comprobar si se terminó el juego
            if (wrongGuesses === maxWrongGuesses) { // Si se alcanzan 6 fallos
                document.getElementById('message').textContent = "¡Perdiste! La palabra era: " + wordToGuess;
            }
        }
    }
}

// Dibujar el ahorcado paso a paso según los fallos
function drawHangmanStep(step) {
    // Dibuja las partes del ahorcado de acuerdo al número de fallos
    if (step === 1) {
        ctx.beginPath();
        ctx.moveTo(150, 50);
        ctx.lineTo(150, 350); // Dibujar la cuerda
        ctx.stroke();
    } else if (step === 2) {
        ctx.beginPath();
        ctx.moveTo(150, 50);
        ctx.lineTo(250, 50); // Dibujar la barra horizontal
        ctx.stroke();
    } else if (step === 3) {
        ctx.beginPath();
        ctx.moveTo(200, 50);
        ctx.lineTo(200, 70); // Dibujar la base
        ctx.stroke();
    } else if (step === 4) {
        ctx.beginPath();
        ctx.arc(200, 100, 30, 0, Math.PI * 2); // Dibujar la cabeza
        ctx.stroke();
    } else if (step === 5) {
        ctx.beginPath();
        ctx.moveTo(200, 130);
        ctx.lineTo(200, 180); // Dibujar el cuerpo
        ctx.stroke();
    } else if (step === 6) {
        ctx.beginPath();
        ctx.moveTo(200, 150);
        ctx.lineTo(170, 180); // Brazo izquierdo
        ctx.moveTo(200, 150);
        ctx.lineTo(230, 180); // Brazo derecho
        ctx.moveTo(200, 180);
        ctx.lineTo(170, 210); // Pierna izquierda
        ctx.moveTo(200, 180);
        ctx.lineTo(230, 210); // Pierna derecha
        ctx.stroke();
    }
}

// Iniciar el juego
initializeGame();
