let historyStack = [];

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
