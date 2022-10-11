const valores = window.location.search;
const cuotas = document.querySelectorAll(".cuotas > input[type='radio']")
const combos = document.querySelectorAll(".combos > input[type='radio']")
// const form_inputs = document.querySelectorAll(".filters_container > form label")
const button = document.getElementById("button_filter")



if(valores != ""){
    document.getElementById('clear').style.visibility = 'visible';
}else{
    document.getElementById('clear').style.visibility = 'hidden';
}

if (valores.includes("cuota=3")){
    document.getElementById("tres").checked = true;
    document.getElementById("tres").nextElementSibling.classList.add("check")
}
else if(valores.includes("cuota=6")){
    document.getElementById("seis").checked = true;
    document.getElementById("seis").nextElementSibling.classList.add("check")
}
else if(valores.includes("cuota=12")){
    document.getElementById("doce").checked = true;
    document.getElementById("doce").nextElementSibling.classList.add("check")
}
else if(valores.includes("cuota=24")){
    document.getElementById("venticuatro").checked = true;
    document.getElementById("venticuatro").nextElementSibling.classList.add("check")
}


if (valores.includes("combo=cocina")){
    document.getElementById("cocina").checked = true;
    document.getElementById("cocina").nextElementSibling.classList.add("check")
}
else if(valores.includes("combo=gamer")){
    document.getElementById("gamer").checked = true;
    document.getElementById("gamer").nextElementSibling.classList.add("check")
}
else if(valores.includes("combo=musica")){
    document.getElementById("musica").checked = true;
    document.getElementById("musica").nextElementSibling.classList.add("check")
}
else if(valores.includes("combo=tv")){
    document.getElementById("tv").checked = true;
    document.getElementById("tv").nextElementSibling.classList.add("check")
}


cuotas.forEach(function (e) {
    e.addEventListener("click",()=>{
        if (!e.nextElementSibling.classList.contains("check") ) {
            desactiveCheck_marcas()
            e.nextElementSibling.classList.add("check")
            e.checked = true
        }else if(e.nextElementSibling.classList.contains("check")){
            desactiveCheck_marcas()
            e.checked = false
        }
    } )
});

combos.forEach(function (e) {
    e.addEventListener("click",()=>{
        if (!e.nextElementSibling.classList.contains("check") ) {
            desactiveCheck_combos()
            e.nextElementSibling.classList.add("check")
            e.checked = true
        }else if(e.nextElementSibling.classList.contains("check")){
            desactiveCheck_combos()
            e.checked = false
        }
    } )
}); 



function desactiveCheck_marcas() {
    cuotas.forEach(element => element.nextElementSibling.classList.remove("check"));
  }

function desactiveCheck_combos() {
    combos.forEach(element => element.nextElementSibling.classList.remove("check"));
  }