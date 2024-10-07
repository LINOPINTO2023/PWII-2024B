document.addEventListener("DOMContentLoaded", () => {
    
    const programaDiv = document.createElement('div');
    programaDiv.id = 'programa';
    
    const form = document.createElement('form');
    form.name = 'calculador';
    
    const inputDisplay = document.createElement('input');
    inputDisplay.type = 'text';
    inputDisplay.name = 'respuesta';
    inputDisplay.value = '';
    inputDisplay.autocomplete = 'off';
    inputDisplay.readOnly = true;
    form.appendChild(inputDisplay);
    
    const valores = [
        { value: '7', class: 'white' },
        { value: '8', class: 'white' },
        { value: '9', class: 'white' },
        { value: '+', class: 'orange' },
        { value: '4', class: 'white' },
        { value: '5', class: 'white' },
        { value: '6', class: 'white' },
        { value: '-', class: 'orange' },
        { value: '1', class: 'white' },
        { value: '2', class: 'white' },
        { value: '3', class: 'white' },
        { value: 'X', class: 'orange' },
        { value: '0', class: 'white' },
        { value: 'C', class: 'white', type: 'reset' },
        { value: '=', class: 'white' },
        { value: '/', class: 'orange' }
    ];

    
    for (let i = 0; i < valores.length; i += 4) {
        const filaDiv = document.createElement('div');
        filaDiv.className = 'fila';
        
        for (let j = 0; j < 4; j++) {
            const boton = valores[i + j];
            const inputButton = document.createElement('input');
            inputButton.type = boton.type || 'button';
            inputButton.value = boton.value;
            inputButton.className = boton.class;

            if (boton.value === 'C') {
                inputButton.onclick = function() { limpiar(); };
            } else if (boton.value === '=') {
                inputButton.onclick = function() { resultado(); };
            } else {
                const displayValue = boton.value === 'X' ? '*' : boton.value;
                inputButton.onclick = function() { agregarValor(displayValue); };
            }

            filaDiv.appendChild(inputButton);
        }
        
        form.appendChild(filaDiv);
    }

    programaDiv.appendChild(form);

    const pilaDiv = document.createElement('div');
    pilaDiv.className = 'pila';
    pilaDiv.id = 'pila';

    const pilaHeader = document.createElement('h2');
    pilaHeader.textContent = 'Pila de operaciones:';

    const pilaLista = document.createElement('ul');
    pilaLista.id = 'lista-pila';

    pilaDiv.appendChild(pilaHeader);
    pilaDiv.appendChild(pilaLista);

    document.body.appendChild(programaDiv);
    document.body.appendChild(pilaDiv);
});
