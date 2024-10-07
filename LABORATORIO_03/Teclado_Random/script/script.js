
document.addEventListener('DOMContentLoaded', (event) => {
    const formulario = document.getElementById('formulario');
    const teclado = document.getElementById('teclado');
    const clave = document.getElementById('clave');

    function generarNumerosRandom() {
        const numbers = Array.from({ length: 10 }, (_, i) => i);
        for (let i = numbers.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
        }
        return numbers;
    }
});