const button_submit = document.getElementById("form_product_button")
const inputs_form = document.querySelectorAll("#form_fetch_post input[type='text'], #form_fetch_post input[type='email'], #form_fetch_post input[type='file']")
const message_success = document.querySelector(".form_success_wrapper")
const message_error = document.querySelector(".form_error_wrapper")
const button_close_error = document.querySelector("#close_form_error")
const button_close_success = document.querySelector("#close_form_success")

button_submit.addEventListener("click", EnviarDatos)
button_close_error.addEventListener("click",()=>{
    message_error.classList.remove("show")
    
})
button_close_success.addEventListener("click",()=>{
    message_success.classList.remove("show")
    
})

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
    var form = new FormData(document.querySelector(".form"))

    let post = fetch(url,{
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if (data) {
            LimpiarDatos()
            message_error.classList.add("show")
            parent_cv.removeChild(cv_element)
            image_cv.setAttribute("src","/static/images/icons/cv_icon.svg")
        }
    }).catch(error => {
        LimpiarDatos()
        message_error.classList.remove("show")
        message_success.classList.add("show")
        parent_cv.removeChild(cv_element)
        image_cv.setAttribute("src","/static/images/icons/cv_icon.svg")
        // image_cv.setAttribute("src","/static/images/icons/cv_icon.svg")
    })
    
}

function LimpiarDatos() {
    inputs_form.forEach(element => {
        element.value = ""
    });
    button_submit.classList.add("desactive")
}