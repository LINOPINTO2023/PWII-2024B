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