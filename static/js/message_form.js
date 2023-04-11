let input_target = document.querySelector("#objetivo")
// console.table(input_target)

let input_target_monto = input_target.offsetParent.children[2].children[0].children[1].children[0].textContent
console.table(input_target_monto)
// let input_target_cuotas = input_target.offsetParent.children[0].children[1].childNodes[3].textContent

input_target_monto = "Solicitud de dinero de " + input_target_monto

input_target.value = input_target_monto



