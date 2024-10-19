let captchaText = '';

//Función para agregar números al input del teclado virtual
function addToInput(value) {
    const input = document.getElementById('clave-virtual');
    if (input.value.length < 6) {  //Limitar a 6 caracteres
        input.value += value;
    }
}

//Función para limpiar el input del teclado virtual
function clearInput() {
    const input = document.getElementById('clave-virtual');
    input.value = '';
}

function randomTeclado() {
    const teclado = document.getElementById('teclado');
    const buttons = Array.from(teclado.querySelectorAll('button'));
    //Excluimos el botón "LIMPIAR" del shuffle
    const numberButtons = buttons.filter(button => button.textContent !== "LIMPIAR");
    //Desordenamos los botones numéricos aleatoriamente
    numberButtons.sort(() => Math.random() - 0.5);
    //Insertamos los botones desordenados nuevamente en el DOM
    numberButtons.forEach(button => teclado.insertBefore(button, teclado.firstChild));
}

//Función para generar el CAPTCHA aleatorio
function generateCaptcha() {
    const canvas = document.getElementById('captchaCanvas');
    const ctx = canvas.getContext('2d');

    //Limpiamos el canvas antes de dibujar el nuevo CAPTCHA
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    //Generamos una cadena aleatoria de 6 caracteres (letras y números)
    const charsArray = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lengthOtp = 6;
    captchaText = '';
    for (let i = 0; i < lengthOtp; i++) {
        captchaText += charsArray[Math.floor(Math.random() * charsArray.length)];
    }

    // Dibujamos el CAPTCHA en el canvas
    ctx.font = '30px Arial';
    ctx.fillStyle = '#000';
    ctx.fillText(captchaText, 10, 35);

}

//Validación del formulario
document.getElementById('loginForm').addEventListener('submit', function (event) {
    const cardNumber = document.getElementById('card-number').value;
    const documentNumber = document.getElementById('document-number').value;
    const claveVirtual = document.getElementById('clave-virtual').value;
    const captcha = document.querySelector('input[name="captcha"]').value;
    const errorMessage = document.getElementById('error-message');

    //Función para mostrar el mensaje de error dinámicamente
    function showError(message) {
        const errorMessage = document.createElement('div');
        errorMessage.classList.add('dynamic-error-message');
        errorMessage.style.color = 'red';
        errorMessage.style.marginBottom = '10px';
        errorMessage.textContent = message;
        const form = document.getElementById('loginForm');
        form.insertBefore(errorMessage, form.firstChild);  
    }

    //Verificamos que los valores sean numéricos
    if (isNaN(cardNumber) || isNaN(documentNumber)) {
        event.preventDefault(); 
        showError('Por favor, ingrese solo números en los campos de tarjeta y documento.');
        return;
    }

    //Verificamos que todos los campos estén llenos
    if (!cardNumber || !documentNumber || !claveVirtual || !captchaInput) {
        event.preventDefault(); 
        showError('Por favor, llena todos los campos.');
        randomTeclado();
        return;
    }
    //Validamos el CAPTCHA
    if (captchaInput !== captchaText) {
        event.preventDefault();
        showError('El texto del CAPTCHA no coincide. Inténtalo de nuevo.');
        generateCaptcha();
        return;
    }
});

window.onload = function () {
    generateCaptcha();
};








