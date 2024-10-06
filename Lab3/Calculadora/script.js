const display = document.querySelector('.display');
let currentValue = '';
let operator = '';
let previousValue = '';
let stack = [];
const buttons = document.querySelectorAll('button');
buttons.forEach(button => {
    button.addEventListener('click', function() {
        const buttonId = this.id;

        if (buttonId === 'C') {
            clearDisplay();
        }
        else if (buttonId === 'Del') {
            deleteNumber();
        }
        else if (buttonId === '=') {
            calcular();
        }
        else if (buttonId === 'sqrt') {
            sqrt();
        }
        else if (['+', '-', '*', '/', '**'].includes(buttonId)) {
            operador(buttonId);
        }
        else {
            incluirNumero(buttonId);
        }
    });
});

function clearDisplay() {
    currentValue = '';
    operator = '';
    previousValue = '';
    display.value = '';
}

function deleteNumber() {
    currentValue = currentValue.slice(0, -1);
    display.value = currentValue;
}

function calcular() {
    if (previousValue && currentValue && operator) {
        const result = eval(previousValue + operator + currentValue);
        display.value = result;
        stack.push(`${previousValue} ${operator} ${currentValue} = ${result}`);
        updateStackDisplay();
        previousValue = eval(previousValue + operator + currentValue);
        display.value = previousValue;
        currentValue = '';
        operator = '';
    }
}

function sqrt() {
    if (currentValue) {
        currentValue = Math.sqrt(parseFloat(currentValue)).toString();
        display.value = currentValue;
        stack.push(`sqrt(${currentValue}) = ${currentValue}`);
        updateStackDisplay();
    }
}

function operador(op) {
    if (currentValue && !previousValue) {
        previousValue = currentValue;
        operator = op === '**' ? '**' : op;
        currentValue = '';
    }
}

function incluirNumero(num) {
    if (num === '.' && currentValue.includes('.')) return;
    currentValue += num;
    display.value = currentValue;
}
function updateStackDisplay() {
    const stackDisplay = document.querySelector('.stack'); 
    stackDisplay.innerHTML = stack.join('<br>'); 
}