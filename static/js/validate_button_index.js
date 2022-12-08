const inputs = document.querySelectorAll(".form_cliente > input[type='text']")
const input_array = Array.from(inputs)

const input_submit = document.querySelector(".form_cliente > #enviar")



window.addEventListener("keypress", function(event){
    if (event.keyCode == 13){
        event.preventDefault();
    }
}, false);

inputs.forEach(element => {
    element.addEventListener("change",()=>{
        let list_valid = input_array.filter(input => input.value != "") 
        console.log(list_valid)
        
        if (list_valid.length == 6){
            console.log("se desbloquea")
            input_submit.classList.remove("desactive")
        }
        else{
            input_submit.classList.add("desactive")
        }
    })
});