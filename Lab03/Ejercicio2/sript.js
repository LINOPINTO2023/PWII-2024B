// Obtener referencia al campo de texto donde se muestran las operaciones

//variables
const elemento = document.querySelector('input[type="text"]');
let ActualVariable = "";
// Referencia al historial
const historialElement = document.getElementById('historial'); 
let historial = [];

// Asignar la funcionalidad a los botones
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
        const value = button.textContent.trim();

        if (value === "=") {
            calculate();
        } else if (value === "⌫") {
            deleteLast();
        } else if (value === "Deshacer") {
            clearAll();
        } else if (value === "x²") {
            ActualVariable += "^2";
            elemento.value = ActualVariable;
        } else if (value === "%") {
            ActualVariable = ActualVariable/100;
            elemento.value = ActualVariable;
        }
        else {
            ActualizarVariable(value);
        }
    });
});

// Función para actualizar el display
function ActualizarVariable(value) {
    ActualVariable += value;
    elemento.value =  ActualVariable;
}

// Función para evaluar la operación y mostrar el resultado
function calculate() {
    try {
        //Creamos una variable que almacenará la operación antes de reemplazar sus símbolos
        let resultHistorial = ActualVariable;
        // Reemplazar símbolos para que sean compatibles con JavaScript
        let result = ActualVariable
            .replace("÷", "/")
            .replace("x", "*")
            .replace("mod", "%")
            .replace("π", Math.PI)
            .replace("√", "Math.sqrt(")
            .replace("^2", "**2")
            .replace("E", "*Math.E")

        if (result.includes("Math.sqrt(")) result += ")"; // Cerrar la raíz cuadrada si está presente
        elemento.value = eval(result); // Evaluar la operación
        ActualVariable = elemento.value; // Actualizar la operación con el resultado

         // Actualizar la pila del historial, añadir el nuevo cálculo
         historial.push(resultHistorial + " = " + ActualVariable);

         // Limitar el historial a 3 operaciones para la construcción de la pila
         if (historial.length > 3) {
             historial.shift(); // Si supera las 3 operaciones en la calculadora, se irá eliminando la operación más antigua
         }
 
         // Mostrar el historial en la página
         historialElement.innerHTML = historial.join('<br>');

    } catch (error) {
        display.value = "Error"; // Mostrar error en caso de una operación inválida
        ActualVariable = ""; // Reiniciar operación
    }

    
}// Función para limpiar el último carácter
function deleteLast() {
    ActualVariable = ActualVariable.slice(0, -1);
    elemento.value = ActualVariable || "0";
}

// Función para limpiar todo
function clearAll() {
    ActualVariable = "";
    elemento.value = "0";
}