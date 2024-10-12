// Elementos del DOM
const display = document.getElementById('display');
const buttons = document.getElementById('buttons');
const historyList = document.getElementById('historyList');
let currentExpression = '';
let displayExpression = '';
const operationStack = [];

buttons.addEventListener('click', event => {
    const target = event.target;
    if (target.matches('button')) {
        const action = target.dataset.action;
        const value = target.dataset.num;

        if (action) {
            handleAction(action);
        } else if (value) {
            appendToExpression(value);
        }

        updateDisplay();
    }
});
// Manejar acciones (operadores y funciones especiales)
function handleAction(action) {
    switch (action) {
        case '+':
        case '-':
        case '*':
        case '/':
            appendToExpression(action);
            break;
        case 'mod':
            appendToExpression(' mod ');
            break;
        case '=':
            calculateResult();
            break;
        case 'clear':
            clearCalculator();
            break;
        case 'delete':
            deleteLastChar();
            break;
        case 'π':
            appendToExpression('π');
            break;
        case '√':
            appendToExpression('√(');
            break;
        case '^2':
            appendToExpression('^2');
            break;
        case 'porcent':
            handlePercent();
            break;
        case '(':
        case ')':
            appendToExpression(action);
            break;
    }
}
// Agregar a la expresión
function appendToExpression(value) {
    currentExpression += value;
    displayExpression += value;
}
function calculateResult() {
    if (currentExpression === '') return;
    try {
        let expressionToEvaluate = currentExpression
            .replace(/π/g, 'Math.PI')
            .replace(/√\(/g, 'Math.sqrt(')
            .replace(/\^2/g, '**2')
            .replace(/%/g, '/100')
            .replace(/mod/g, '%');

        const result = eval(expressionToEvaluate);
        const roundedResult = Number(result.toFixed(10));

        const operation = `${displayExpression} = ${roundedResult}`;
        operationStack.push(operation);
        updateHistory();
        currentExpression = roundedResult.toString();
        displayExpression = roundedResult.toString();
    } catch (error) {
        currentExpression = 'Error';
        displayExpression = 'Error';
    }
}
// Limpiar calculadora
function clearCalculator() {
    currentExpression = '';
    displayExpression = '';
}

// Borrar último carácter
function deleteLastChar() {
    currentExpression = currentExpression.slice(0, -1);
    displayExpression = displayExpression.slice(0, -1);
}
// Manejar porcentaje
function handlePercent() {
    appendToExpression('/100');
}
// Actualizar pantalla
function updateDisplay() {
    display.value = displayExpression || '0';
}
// Actualizar historial
function updateHistory() {
    historyList.innerHTML = '';
    operationStack.slice().reverse().forEach(operation => {
        const li = document.createElement('li');
        li.textContent = operation;
        historyList.appendChild(li);
    });
}
