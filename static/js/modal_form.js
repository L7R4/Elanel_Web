const contactos = document.querySelectorAll(".contacto h2");
var numbers_heights = document.getElementsByClassName('numbers');
const open_modal = document.querySelectorAll(".beneficios__table__item__buttton")
const background_modal = document.querySelector(".modal_form_container")
const modal_window = document.querySelector(".wrapper_windown_form")
const close_modal = document.querySelector("#close_modal");
const plan_value = document.querySelector("#servicio");
const product_value = document.querySelector("#producto");
const monto_value = document.querySelector("#monto");

const service_selected = document.querySelector(".service_selected")
const product_selected = document.querySelector(".product_selected")
const monto_selected = document.querySelector(".monto_selected")
// console.log(clearMonto("$2000/mes"))
open_modal.forEach(element => {
    element.addEventListener("click",()=>{
        background_modal.classList.add("active_modal");
        modal_window.classList.add("active_modal");
        plan_value.value = element.parentElement.childNodes[1].textContent
        product_value.value = element.parentElement.children[3].children[0].children[0].textContent
        monto_value.value = clearMonto(element.parentElement.children[2].textContent) 
        // monto_value.value = Math.trunc(monto_del_producto)
        service_selected.innerText = plan_value.value
        product_selected.innerText = product_value.value
        monto_selected.innerText = "$" + monto_value.value + "/mes"
    })
});

close_modal.addEventListener("click",()=>{
    background_modal.classList.remove("active_modal");
    modal_window.classList.remove("active_modal");
    message_success.classList.add("hide")
})

function clearMonto(monto){
    const numbers = ["0","1","2","3","4","5","6","7","8","9"]
    let number_clear = ""

    for (let i = 0; i < monto.length; i++) {
        if (monto[i] in numbers) {
            number_clear += monto[i]
        }
    }
    return parseInt(number_clear)
}

