const contactos = document.querySelectorAll(".contacto h2");
var numbers_heights = document.getElementsByClassName('numbers');
const open_modal = document.querySelectorAll(".beneficios__table__item__buttton")
const background_modal = document.querySelector(".modal_form_container")
const modal_window = document.querySelector(".wrapper_windown_form")
const close_modal = document.querySelector("#close_modal");
const plan_value = document.querySelector("#servicio");
console.table(plan_value)


open_modal.forEach(element => {
    element.addEventListener("click",()=>{
        background_modal.classList.add("active_modal");
        modal_window.classList.add("active_modal");
        plan_value.value = element.parentElement.childNodes[1].textContent
    })
});

close_modal.addEventListener("click",()=>{
    background_modal.classList.remove("active_modal");
    modal_window.classList.remove("active_modal");
})
