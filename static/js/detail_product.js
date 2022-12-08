complete_image = document.querySelector(".complete__image img");
query_images = document.querySelectorAll(".nav__images figure img")
complete_image.src = query_images[0].src
// message_form = document.querySelector(".form_message")
// form_product = document.querySelector("#form_product")
query_images.forEach(element => {
    element.addEventListener("mouseover", () =>{
        image_url = element.src
        colocarImage(image_url)
    })
});


function colocarImage(url) {
    complete_image.src=url
}

// function form_send(){
//     form_product.preventDefault()
//     message_form.style.zIndex ="2"
// }