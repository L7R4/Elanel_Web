const valores = window.location.search;
const a = window.location
const marcas = document.querySelectorAll(".marcas > input[type='radio']")
const estado = document.querySelectorAll(".estado > input[type='radio']")
const form_inputs = document.querySelectorAll(".filters_container > form label")
const button = document.getElementById("button_filter")

window.addEventListener('load',()=>{
    if(valores != ""){
        document.getElementById('clear').style.visibility = 'visible';
    }else{
        document.getElementById('clear').style.visibility = 'hidden';
    }
    
    if (valores.includes("?marca=yamaha")){
        document.getElementById("yamaha").checked = true;
        document.getElementById("yamaha").nextElementSibling.classList.add("check")
    }
    else if(valores.includes("?marca=corven")){
        document.getElementById("corven").checked = true;
        document.getElementById("corven").nextElementSibling.classList.add("check")
    }
    else if(valores.includes("?marca=rouser")){
        document.getElementById("rouser").checked = true;
        document.getElementById("rouser").nextElementSibling.classList.add("check")
    }
    else if(valores.includes("?marca=motomel")){
        document.getElementById("motomel").checked = true;
        document.getElementById("motomel").nextElementSibling.classList.add("check")
    }
    else if(valores.includes("?marca=honda")){
        document.getElementById("honda").checked = true;
        document.getElementById("honda").nextElementSibling.classList.add("check")
    }
    else if(valores.includes("?marca=zanella")){
        document.getElementById("zanella").checked = true;
        document.getElementById("zanella").nextElementSibling.classList.add("check")
    }
    
    if (valores.includes("status=False")) {
        document.getElementById("nuevo").checked = true;
        document.getElementById("nuevo").nextElementSibling.classList.add("check")
    }else if(valores.includes("status=True")){
        document.getElementById("usado").checked = true;
        document.getElementById("usado").nextElementSibling.classList.add("check")
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

})



function desactiveCheck_marcas() {
    marcas.forEach(element => element.nextElementSibling.classList.remove("check"));
  }
function desactiveCheck_estado() {
    estado.forEach(element => element.nextElementSibling.classList.remove("check"));
  }
    
    


