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