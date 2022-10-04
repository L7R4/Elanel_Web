const url_actual = window.location.href;
const yamaha = document.getElementById('moto_yamaha')
const honda = document.getElementById('moto_honda')
const motomel = document.getElementById('moto_motomel')
const rouser = document.getElementById('moto_rouser')


yamaha.addEventListener("click", ()=>{
    val_modificated = yamaha.href + "motos/?marca=yamaha"
    yamaha.href = val_modificated
})
honda.addEventListener("click", ()=>{
    val_modificated = honda.href + "motos/?marca=honda"
    honda.href = val_modificated
})
motomel.addEventListener("click", ()=>{
    val_modificated = motomel.href + "motos/?marca=motomel"
    motomel.href = val_modificated
})
rouser.addEventListener("click", ()=>{
    val_modificated = rouser.href + "motos/?marca=rouser"
    rouser.href = val_modificated
})