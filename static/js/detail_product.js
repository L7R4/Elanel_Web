complete_image = document.querySelector(".complete__image img");
query_images = document.querySelectorAll(".nav__images figure img")
let button_display_form = document.querySelector(".display_form")
let modal_form = document.querySelector(".form_modal")
let close_buttons_form = document.querySelectorAll(".close_form")


if (complete_image && query_images && query_images.length > 0) {
    complete_image.src = query_images[0].src
}

window.addEventListener('load',()=>{
    if (query_images) {
        query_images.forEach(element => {
            element.addEventListener("mouseover", () =>{
                image_url = element.src
                colocarImage(image_url)
            })
        });
    }
    
    if (button_display_form && modal_form) {
        button_display_form.addEventListener("click", ()=>{
            modal_form.classList.add("active")
        })
    }
    
    if (close_buttons_form) {
        close_buttons_form.forEach(element =>{
            element.addEventListener("click", () => {
                if (element.parentElement && element.parentElement.parentElement) {
                    element.parentElement.parentElement.classList.remove("active")
                }
            })
        })
    }

})

function colocarImage(url) {
    complete_image.src=url
}