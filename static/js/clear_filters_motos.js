const valores = window.location.search;
const a = window.location
// console.log(valores)
// console.log(a)
const marcas = document.querySelectorAll(".marcas > input[type='radio']")
const estado = document.querySelectorAll(".estado > input[type='radio']")
const form_inputs = document.querySelectorAll(".filters_container > form label")
const button = document.getElementById("button_filter")




if(valores != ""){
    document.getElementById('clear').style.visibility = 'visible';
}else{
    document.getElementById('clear').style.visibility = 'hidden';
}

if (valores.includes("marca=yamaha")){
    document.getElementById("yamaha").checked = true;
}
else if(valores.includes("marca=corven")){
    document.getElementById("corven").checked = true;
}
else if(valores.includes("marca=rouser")){
    document.getElementById("rouser").checked = true;
}
else if(valores.includes("marca=motomel")){
    document.getElementById("motomel").checked = true;
}
else if(valores.includes("marca=honda")){
    document.getElementById("honda").checked = true;
}
else if(valores.includes("marca=zanella")){
    document.getElementById("zanella").checked = true;
}

if (valores.includes("status=False")) {
    document.getElementById("nuevo").checked = true;
}else if(valores.includes("status=True")){
    document.getElementById("usado").checked = true;
}

marcas.forEach(function (e) {
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

estado.forEach(function (e) {
    e.addEventListener("click",()=>{
        if (!e.nextElementSibling.classList.contains("check") ) {
            desactiveCheck_estado()
            e.nextElementSibling.classList.add("check")
            e.checked = true
        }else if(e.nextElementSibling.classList.contains("check")){
            desactiveCheck_estado()
            e.checked = false
        }
    } )
}); 

// form_inputs.forEach(function (e) {
//     console.log(e)
//     if(e.classList.contains("check")){
//         console.log("e")
        
//     }
// })

function desactiveCheck_marcas() {
    marcas.forEach(element => element.nextElementSibling.classList.remove("check"));
  }
function desactiveCheck_estado() {
    estado.forEach(element => element.nextElementSibling.classList.remove("check"));
  }
    
    


