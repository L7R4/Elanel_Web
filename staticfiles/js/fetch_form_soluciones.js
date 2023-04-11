const button_submit = document.getElementById("form_product_button")
const inputs_form = document.querySelectorAll("#form_fetch_post  input[type='text'],#form_fetch_post  input[type='email']")
const message_success = document.querySelector(".message_success_wrapper")
const message_error = document.querySelector(".message_error_wrapper")
const close_form_success = document.getElementById("close_form_success")
const close_form_error = document.getElementById("close_form_error")
var url = window.location.pathname;

window.addEventListener('load',()=>{
    button_submit.addEventListener("click", EnviarDatos)

    close_form_success.addEventListener("click", ()=>{
        message_success.classList.remove("active")
    })
    close_form_error.addEventListener("click", ()=>{
        message_error.classList.remove("active")
    })
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    function EnviarDatos() {
        var form = new FormData(document.getElementById("form_fetch_post"))
    
        let post = fetch(url,{
            method: "POST",
            body: form,
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data) {
                LimpiarDatos()
                message_success.classList.remove("active")
                message_error.classList.add("active")
                // input_target.value = input_target_moto
            }
        }).catch(error => {
            LimpiarDatos()
            message_error.classList.remove("active")
            message_success.classList.add("active")
        })
        
        
    }

})

function LimpiarDatos() {
    inputs_form.forEach(element => {
        element.value = ""
    });
    button_submit.classList.add("desactive")
}