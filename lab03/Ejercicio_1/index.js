const buttonContainer = document.getElementById("buttonContainer");

function CrearBotones() {
  const inputClave = document.querySelector(".columnContent input");
  const numeros = [...Array(10).keys()];

  numeros.sort(() => Math.random() - 0.5);

  numeros.forEach((i) => {
    const boton = document.createElement("button");

    boton.textContent = i;
    boton.className = "button";
    boton.addEventListener("click", () => {
      inputClave.value += i;
    });

    buttonContainer.appendChild(boton);
  });
  const limpiar = document.createElement("button");
  limpiar.textContent = "LIMPIAR";
  limpiar.className = "button";

  limpiar.addEventListener("click", () => {
    inputClave.value = "";
  });

  buttonContainer.appendChild(limpiar);
}
CrearBotones();
