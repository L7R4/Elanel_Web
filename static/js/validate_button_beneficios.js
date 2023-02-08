const inputs = document.querySelectorAll(".window_form > form > input[type='text'],.window_form > form >  input[type='email'],.window_form > form >  input[type='number']")
console.log(inputs)

const input_array = Array.from(inputs)

const input_submit = document.querySelector(".window_form > form  > #form_product_button")



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