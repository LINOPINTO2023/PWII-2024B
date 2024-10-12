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