const inputs = document.querySelectorAll("#form_product > input[type='text'],#form_product > input[type='email']")
console.log(inputs)

const input_array = Array.from(inputs)

const input_submit = document.querySelector("#form_product > #form_product_button")



window.addEventListener("keypress", function(event){
    if (event.keyCode == 13){
        event.preventDefault();
    }
}, false);

inputs.forEach(element => {
    element.addEventListener("change",()=>{
        let list_valid = input_array.filter(input => input.value != "") 
        console.log(list_valid)
        
        if (list_valid.length == 4){
            console.log("se desbloquea")
            input_submit.classList.remove("desactive")
        }
        else{
            input_submit.classList.add("desactive")
        }
    })
});