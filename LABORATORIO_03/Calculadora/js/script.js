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
        pila.push(operacionActual + ' = ' + resultado);
        actualizarPila();
        operacionActual = '';
        document.calculador.respuesta.value = resultado;
    } catch (e) {
        document.calculador.respuesta.value = 'Error';
    }
}

function actualizarPila() {
    let listaPila = document.getElementById('lista-pila');
    listaPila.innerHTML = '';
    pila.forEach(function (operacion) {
        let li = document.createElement('li');
        li.textContent = operacion;
        listaPila.appendChild(li);
    });
}
