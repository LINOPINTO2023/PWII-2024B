const display = document.querySelector(".display");
const buttons = document.querySelectorAll("button"); 

buttons.forEach(buttons => {
    buttons.addEventListener("click", function() {
        const btnId = buttons.id;
        if (btnId === "=") {
            try {
                result = eval(display.value);
                if (result % 1 !== 0){
                    display.value=result.toFixed(2);
                } else {
                    display.value=eval(display.value);
                }
            } catch (e) {
                display.value = "Write a correct expression";
            }
        } else if (btnId === "C") {
            display.value = "";
        } else if (btnId === "Del") {
            display.value = display.value.slice(0, -1);
        } else if(btnId==="Math.sqrt(") {
            display.value += "Math.sqrt(";
        } else {
            display.value += btnId;
        }
    });
});



