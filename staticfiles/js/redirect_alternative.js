const url_actual = window.location.href;
const yamaha = document.getElementById('moto_yamaha')
const honda = document.getElementById('moto_honda')
const motomel = document.getElementById('moto_motomel')
const rouser = document.getElementById('moto_rouser')
const combo_cocina = document.getElementById('combo_cocina')
const combo_gamer = document.getElementById('combo_gamer')
const combo_musica = document.getElementById('combo_musica')
const combo_tv = document.getElementById('combo_tv')


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

combo_cocina.addEventListener("click", ()=>{
    val_modificated = combo_cocina.href + "elec/?combo=cocina"
    combo_cocina.href = val_modificated
})
combo_gamer.addEventListener("click", ()=>{
    val_modificated = combo_gamer.href + "elec/?combo=gamer"
    combo_gamer.href = val_modificated
})
combo_musica.addEventListener("click", ()=>{
    val_modificated = combo_musica.href + "elec/?combo=musica"
    combo_musica.href = val_modificated
})
combo_tv.addEventListener("click", ()=>{
    val_modificated = combo_tv.href + "elec/?combo=tv"
    combo_tv.href = val_modificated
})