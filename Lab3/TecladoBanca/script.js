const buttons = document.querySelectorAll(".button");
const numbers = [];

buttons.forEach(button => {
  let num;
  do {
    num = Math.floor(Math.random() * 10) + 1;
  } while (numbers.includes(num));
  numbers.push(num);
  button.innerHTML = num;
});
