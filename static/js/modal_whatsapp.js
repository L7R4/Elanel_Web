const contactos = document.querySelectorAll(".contacto h2");
var numbers_heights = document.getElementsByClassName('numbers');
const open_modal = document.querySelector("#whatsapp_contact")
const background_modal = document.querySelector(".modal_whatsapp_container")
const modal_window = document.querySelector(".wrapper_windown_whatsapp")
const close_modal = document.querySelector("#close_modal");



open_modal.addEventListener("click",()=>{
    background_modal.classList.add("active_modal");
    modal_window.classList.add("active_modal");
})
close_modal.addEventListener("click",()=>{
    background_modal.classList.remove("active_modal");
    modal_window.classList.remove("active_modal");
})

contactos.forEach(element => {
    element.addEventListener('click', ()=>{
        const height = element.nextElementSibling.scrollHeight;
        element.classList.toggle('active')
        if (element.classList.contains('active')) {
            element.nextElementSibling.style.maxHeight = height +'px'
            element.nextElementSibling.style.padding = '1% 0'
        }else{
            element.nextElementSibling.style.maxHeight = '0px'
            element.nextElementSibling.style.padding = '0'
        }
    });
});