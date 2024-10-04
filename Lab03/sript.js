// Obtener referencia al campo de texto donde se muestran las operaciones
const elemento = document.querySelector('input[type="text"]');

let ActualVariable = "";

// Función para actualizar el display
function ActualizarVariable(value) {
    ActualVariable += value;
    elemento.value =  ActualVariable;
}

// Función para evaluar la operación y mostrar el resultado
function calculate() {
    try {
        // Reemplazar símbolos para que sean compatibles con JavaScript
        let result = ActualVariable
            .replace("÷", "/")
            .replace("x", "*")
            .replace("mod", "%")
            .replace("π", Math.PI)
            .replace("√", "Math.sqrt(")
            .replace("^2", "**2")
            .replace("E", "*Math.E")
            .replace("%", "/");

        if (result.includes("√")) result += ")"; // Cerrar la raíz cuadrada si está presente
        elemento.value = eval(result); // Evaluar la operación
        ActualVariable = elemento.value; // Actualizar la operación con el resultado
    } catch (error) {
        display.value = "Error"; // Mostrar error en caso de una operación inválida
        ActualVariable = ""; // Reiniciar operación
    }
}
