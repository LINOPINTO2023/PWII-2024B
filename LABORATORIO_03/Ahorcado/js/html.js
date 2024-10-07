document.addEventListener("DOMContentLoaded", () => {
    
    const titulo = document.createElement('h1');
    titulo.textContent = 'Juego del Ahorcado';
    document.body.appendChild(titulo);

    
    const canvas = document.createElement('canvas');
    canvas.id = 'cuadro';
    canvas.width = 400;
    canvas.height = 400;
    document.body.appendChild(canvas);

    const divInput = document.createElement('div');

    const label = document.createElement('label');
    label.htmlFor = 'letra';
    label.textContent = 'Introduce una letra: ';
    divInput.appendChild(label);

    const input = document.createElement('input');
    input.type = 'text';
    input.id = 'letra';
    input.maxLength = 1;
    input.onkeypress = function(event) { teclaPresionada(event); };
    divInput.appendChild(input);

    document.body.appendChild(divInput);
    
    const palabraParrafo = document.createElement('p');
    palabraParrafo.id = 'palabra';
    document.body.appendChild(palabraParrafo);

    const mensajeParrafo = document.createElement('p');
    mensajeParrafo.id = 'mensaje';
    document.body.appendChild(mensajeParrafo);

    
    const script = document.createElement('script');
    script.src = 'js/script_obfuscated.js';
    document.body.appendChild(script);
});
