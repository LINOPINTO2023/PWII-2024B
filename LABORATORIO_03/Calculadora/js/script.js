let operacionActual = '';
let pila = [];

function agregarValor(value) {
    operacionActual += value;
    document.calculador.respuesta.value = operacionActual;
}

function limpiar() {
    operacionActual = '';
    document.calculador.respuesta.value = '';
}

function resultado() {
    try {
        let resultado = eval(operacionActual);
    } catch (e) {
        document.calculador.respuesta.value = 'Error';
    }
}
