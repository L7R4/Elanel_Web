const button_submit = document.getElementById("form_product_button")
const inputs_form = document.querySelectorAll(".window_form > #form_fetch_post input[type='text'] , .window_form > #form_fetch_post input[type='email']")
const message_success = document.querySelector(".message_success")
const message_error = document.querySelector(".message_error")

var url = window.location.pathname;
window.addEventListener('load',()=>{
    button_submit.addEventListener("click", EnviarDatos)
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
        var form = new FormData(document.querySelector(".window_form > form"))
    
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
                message_error.classList.remove("hide")
            }
        }).catch(error => {
            LimpiarDatos()
            message_error.classList.add("hide")
            message_success.classList.remove("hide")
        })
        
    }
    
    function LimpiarDatos() {
        for (let i = 1; i < inputs_form.length; i++) {
            const element = inputs_form[i];
            element.value = ""
            
        }
        // inputs_form.forEach(element => {
        //     element.value = ""
        // });
        button_submit.classList.add("desactive")
    }

})