const button_submit = document.getElementById("form_product_button")
const inputs_form = document.querySelectorAll("#form_product > input[type='text'],#form_product > input[type='email']")
const message_success = document.querySelector(".message_success")

button_submit.addEventListener("click", EnviarDatos)
var url = window.location.pathname;

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
    var form = new FormData(document.getElementById("form_product"))

    let post = fetch(url,{
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken')
        }
    })
    LimpiarDatos()
    message_success.classList.remove("hide")
    
}

function LimpiarDatos() {
    inputs_form.forEach(element => {
        element.value = ""
    });
    button_submit.classList.add("desactive")
}