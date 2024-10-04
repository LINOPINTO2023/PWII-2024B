const display = document.querySelector(".display");
const buttons = document.querySelectorAll("button"); 

buttons.forEach(button => {
    button.addEventListener("click", function() {
        const btnId = button.id;
        if (btnId === "=") {
            try {
                let result = eval(display.value);
                if (result % 1 !== 0) {
                    display.value = result.toFixed(2); 
                } else {
                    display.value = result;
                }
            } catch (e) {
                display.value = "Write a correct expression";
            }
        } else if (btnId === "C") {
            display.value = ""; 
        } else if (btnId === "Del") {
            display.value = display.value.slice(0, -1); 
        } else if (btnId === "sqrt") {
            if (display.value) {
                try {
                    let result = Math.sqrt(parseFloat(display.value)); 
                    display.value = result.toFixed(2);
                } catch (e) {
                    display.value = "Invalid input";
                }
            }
        } else {
            display.value += btnId; 
        }
    });
});
