let display = document.getElementById('display');
let operationStack = [];

// Agrega un carácter al display
function addToDisplay(value) {
  if (value === 'x') {
    // Si el valor es 'x', eliminamos el último carácter del display
    display.value = display.value.slice(0, -1);
  } else {
    // Si no es 'x', agregamos el valor al display
    display.value += value;
  }
}

// Limpia el display
function clearDisplay() {
  display.value = '';
}

// Realiza el cálculo
function calculate() {
  try {
    // Reemplazar 'mod' por '%' para usar eval
    let expression = display.value
      .replace(/mod/g, '%')               // Cambia 'mod' por '%'
      .replace(/ln/g, 'Math.log')         // Cambia 'ln' por 'Math.log'
      .replace(/sqrt\(/g, 'Math.sqrt(')   // Cambia 'sqrt(' por 'Math.sqrt('
      .replace(/\^/g, '**');               // Cambia '^' por '**' para la exponenciación
    
    let result = eval(expression);
    operationStack.push(display.value + ' = ' + result);
    display.value = result;

    // Actualizamos la pila en la página
    updateStack();
  } catch (e) {
    display.value = 'Error';
  }
}

// Actualiza la lista de operaciones en la pila
function updateStack() {
  const stackElement = document.getElementById('operationStack');
  stackElement.innerHTML = '';

  // Mostramos las operaciones guardadas en la pila
  operationStack.forEach(operation => {
    let li = document.createElement('li');
    li.textContent = operation;
    stackElement.appendChild(li);
  });
}

// Cambia el color de la calculadora
function changeCalculatorColor() {
  const color = document.getElementById('colorPicker').value;
  document.querySelector('.calculator').style.backgroundColor = color;
}
