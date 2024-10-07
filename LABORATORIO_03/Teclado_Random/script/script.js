
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

    function crearTeclado() {
        const numeros = generarNumerosRandom();
        teclado.innerHTML = '';

        numeros.forEach(number => {
            const button = document.createElement('button');
            button.type = 'button'; 
            button.textContent = number;
            button.addEventListener('click', (event) => {
                event.preventDefault(); 
                if (clave.value.length < 6) {
                    clave.value += number;
                }
            });
            teclado.appendChild(button);
        });

        const clearButton = document.createElement('button');
        clearButton.type = 'button'; 
        clearButton.textContent = 'LIMPIAR';
        clearButton.addEventListener('click', (event) => {
            event.preventDefault(); 
            clave.value = '';
        });
        teclado.appendChild(clearButton);
    }

    crearTeclado();

    formulario.addEventListener('submit', (event) => {
        event.preventDefault();
        
        console.log("Formulario enviado, clave:", clave.value);
    });
});