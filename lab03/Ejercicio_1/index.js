const buttonContainer = document.getElementById("buttonContainer");

function CrearBotones() {
  const inputClave = document.querySelector(
    ".columnContent input[type='number']"
  );
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
  limpiar.className = "button limpiar";

  limpiar.addEventListener("click", () => {
    inputClave.value = "";
    clearMessages();
  });

  buttonContainer.appendChild(limpiar);
}

CrearBotones();

const ingresarButton = document.querySelector("button[type='button']");
const inputNumeroTarjeta = document.querySelector(
  ".contentInput input[type='number']"
);
const inputTipoDocumento = document.querySelectorAll(".contentInput select")[1];
const inputClave = document.querySelector(
  ".columnContent input[type='number']"
);
const messageContainer = document.createElement("div");
messageContainer.className = "message-container";
document.querySelector(".columnContent").appendChild(messageContainer);

function clearMessages() {
  messageContainer.innerHTML = "";
}

ingresarButton.addEventListener("click", () => {
  clearMessages();

  const numeroTarjeta = inputNumeroTarjeta.value;
  const tipoDocumento = inputTipoDocumento.value;
  const clave = inputClave.value;

  if (!numeroTarjeta || !tipoDocumento || !clave) {
    const errorMessage = document.createElement("p");
    errorMessage.textContent = "Por favor, llena todos los datos requeridos.";
    errorMessage.style.color = "red";
    messageContainer.appendChild(errorMessage);
  } else if (clave.length !== 6) {
    const errorMessage = document.createElement("p");
    errorMessage.textContent = "Por favor, ingresa 6 dígitos en la clave.";
    errorMessage.style.color = "red";
    messageContainer.appendChild(errorMessage);
  } else {
    const successMessage = document.createElement("p");
    successMessage.textContent = "Ingreso exitoso.";
    successMessage.style.color = "green";
    messageContainer.appendChild(successMessage);
  }
});
