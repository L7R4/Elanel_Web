const button_submit = document.getElementById("enviar")
const inputs_form = document.querySelectorAll(".form_cliente > input[type='text']")
const form_success = document.querySelector(".form_success")
const close_form_success = document.getElementById("close_form_success")

button_submit.addEventListener("click", EnviarDatos)

close_form_success.addEventListener("click", ()=>{
    form_success.classList.remove("active")
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
    var form = new FormData(document.getElementById("form_cliente"))

    let post = fetch("/",{
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken')
        }
    })
    console.log(form.keys)
    LimpiarDatos()
    form_success.classList.add("active")
    
}

function LimpiarDatos() {
    inputs_form.forEach(element => {
        element.value = ""
    });
    button_submit.classList.add("desactive")
}


