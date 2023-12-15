const inputs = document.querySelectorAll("#form_fetch_post input[type='text'],#form_fetch_post input[type='email'], #form_fetch_post input[type='file']")
// console.log(inputs)

const input_email = document.querySelector("#form_fetch_post #email")


const length_inputs  = inputs.length

const input_array = Array.from(inputs)

const input_submit = document.querySelector("#form_fetch_post  #form_product_button")


function validate_buttons_form(inputs_var,cant_inputs,input_submit_var){
    window.addEventListener("keypress", function(event){
        if (event.keyCode == 13){
            event.preventDefault();
        }
    }, false);
    
    inputs_var.forEach(element => {
        element.addEventListener("change",()=>{
            let list_valid = Array.from(inputs_var).filter(input => input.value != "")
            
            if (list_valid.length == cant_inputs){
                input_submit_var.classList.remove("desactive")
            }
            else{
                input_submit_var.classList.add("desactive")
            }
        })
    });
}

validate_buttons_form(inputs,length_inputs,input_submit)

input_email.addEventListener("change", ()=> {
    validateEmail(input_email)
})


function validateEmail(value){
	
	// Define our regular expression.
	var validEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;

	// Using test we can check if the text match the pattern
	if( validEmail.test(value.value) ){
        value.classList.remove("invalid")
		return true;

	}else{
        value.classList.add("invalid")
		return false;
	}
}
