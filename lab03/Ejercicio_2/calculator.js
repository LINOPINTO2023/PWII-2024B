let historyStack = [];

function crearCalculadora() {
  const container = document.querySelector(".calculator");

  const display = document.createElement("input");
  display.setAttribute("type", "text");
  display.setAttribute("id", "display");
  display.disabled = true;
  container.appendChild(display);

  const buttonsContainer = document.createElement("div");
  buttonsContainer.className = "buttons";

  const botones = [
    { text: "1", onclick: () => appendValue("1") },
    { text: "2", onclick: () => appendValue("2") },
    { text: "3", onclick: () => appendValue("3") },
    { text: "+", onclick: () => appendValue("+") },
    { text: "4", onclick: () => appendValue("4") },
    { text: "5", onclick: () => appendValue("5") },
    { text: "6", onclick: () => appendValue("6") },
    { text: "-", onclick: () => appendValue("-") },
    { text: "7", onclick: () => appendValue("7") },
    { text: "8", onclick: () => appendValue("8") },
    { text: "9", onclick: () => appendValue("9") },
    { text: "*", onclick: () => appendValue("*") },
    { text: "C", onclick: () => clearDisplay() },
    { text: "0", onclick: () => appendValue("0") },
    { text: "=", onclick: () => calculate(), className: "result" },
    { text: "/", onclick: () => appendValue("/") },
  ];

  botones.forEach((botonData) => {
    const button = document.createElement("button");
    button.textContent = botonData.text;
    button.onclick = botonData.onclick;
    button.className =
      botonData.className != undefined ? botonData.className : "button";
    buttonsContainer.appendChild(button);
  });

  container.appendChild(buttonsContainer);
}

crearCalculadora();

function appendValue(value) {
  const display = document.getElementById("display");
  display.value += value;
}

function clearDisplay() {
  const display = document.getElementById("display");
  display.value = "";
}

function calculate() {
  const display = document.getElementById("display");
  try {
    const result = eval(display.value);
    addToHistory(display.value + " = " + result);
    display.value = result;
  } catch (error) {
    display.value = "Error";
  }
}

function addToHistory(operation) {
  historyStack.push(operation);
  updateHistoryDisplay();
}

function updateHistoryDisplay() {
  const historyList = document.getElementById("historyList");
  historyList.innerHTML = "";

  historyStack.forEach((operation) => {
    const li = document.createElement("li");
    li.textContent = operation;
    historyList.appendChild(li);
  });
}
