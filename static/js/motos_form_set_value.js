let input_target = document.querySelector("#objetivo")

let input_target_moto = input_target.offsetParent.children[3].children[0].children[0].textContent

let input_target_marca = input_target.offsetParent.children[3].children[1].children[0].children[1].textContent

let input_target_modelo = input_target.offsetParent.children[3].children[1].children[1].children[1].textContent

let input_target_precio = input_target.offsetParent.children[3].children[0].children[1].textContent

input_target_moto = "Moto " + input_target_moto + " " + input_target_modelo + " " + input_target_marca + " a " + input_target_precio

input_target.value = input_target_moto
