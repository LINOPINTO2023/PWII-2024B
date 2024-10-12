const keyboard = document.getElementById('virtualKeyboard');
const pinInput = document.getElementById('pinInput');
const captchaImageElement = document.getElementById('captchaImage');
const captchaInputElement = document.getElementById('captchaInput');
const refreshCaptchaButton = document.getElementById('refreshCaptcha');
const submitButton = document.getElementById('submitButton');
const keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'C', '0', '⌫'];
const captchaImages = [
    { src: 'captcha1.png', text: 'Prueba1' },
    { src: 'captcha2.png', text: 'Test' },
    { src: 'captcha3.png', text: 'Imagen3' },
    { src: 'captcha4.png', text: 'esuntest' },
    { src: 'captcha5.png', text: '123' }
];
const captchaFolder = 'captcha-images/';
let currentCaptchaText = '';
function getRandomCaptcha() {
    const randomIndex = Math.floor(Math.random() * captchaImages.length);
    const selectedCaptcha = captchaImages[randomIndex];
    currentCaptchaText = selectedCaptcha.text;
    return captchaFolder + selectedCaptcha.src;
}
function updateCaptcha() {
    captchaImageElement.src = getRandomCaptcha();
}

refreshCaptchaButton.addEventListener('click', updateCaptcha);

document.addEventListener('DOMContentLoaded', () => {
    updateCaptcha();
});
function validateCaptcha() {
    const userCaptchaInput = captchaInputElement.value.trim();

    if (userCaptchaInput === currentCaptchaText) {
        alert('Bienvenido Usuario');
        location.reload();
    } else {
        alert('CAPTCHA incorrecto, por favor intente de nuevo');
        updateCaptcha();
    }
}

submitButton.addEventListener('click', (e) => {
    e.preventDefault();
    validateCaptcha();
});
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function renderKeyboard() {
    keyboard.innerHTML = '';
    shuffleArray(keys);
    keys.forEach(key => {
        const button = document.createElement('button');
        button.textContent = key;
        button.className = 'key';
        button.onclick = () => handleKeyPress(key);
        keyboard.appendChild(button);
    });
}
function handleKeyPress(key) {
    if (key === 'C') {
      pinInput.value = '';
    } else if (key === '⌫') {
      pinInput.value = pinInput.value.slice(0, -1);
    } else if (pinInput.value.length < 6) {
      pinInput.value += key;
    }
  }
  
  renderKeyboard();