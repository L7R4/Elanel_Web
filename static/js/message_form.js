let input_target = document.querySelector("#objetivo")
console.table(input_target)

let input_target_monto = input_target.offsetParent.children[0].children[1].childNodes[1].textContent
let input_target_cuotas = input_target.offsetParent.children[0].children[1].childNodes[3].textContent

input_target_monto = "Solicitud de dinero de " + input_target_monto + " en " + input_target_cuotas

input_target.value = input_target_monto



