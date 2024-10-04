// //document.getElementById("count-el").innerText = 5
// let count = 0 
//   console.log(count)
// let maritza = 17
// let claudia = 2
// let myAge = maritza + claudia

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
function generarNumeros() {
    for (let i = 0; i < 10; i++) {
        const numeroAleatorio = getRandomInt(0, 9);
        document.getElementById(`casilla${i}`).innerText = numeroAleatorio;
    }
}
