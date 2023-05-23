const valores = window.location.search;
const cuotas = document.querySelectorAll(".cuotas > input[type='radio']")
const combos = document.querySelectorAll(".combos > input[type='radio']")
// const form_inputs = document.querySelectorAll(".filters_container > form label")
const button = document.getElementById("button_filter")

window.addEventListener('load',()=>{
    if(valores != ""){
        document.getElementById('clear').style.visibility = 'visible';
    }else{
        document.getElementById('clear').style.visibility = 'hidden';
    }
    
    // if (valores.includes("cuota=24")){
    //     document.getElementById("venticuatro").checked = true;
    //     document.getElementById("venticuatro").nextElementSibling.classList.add("check")
    // }
    // else if(valores.includes("cuota=30")){
    //     document.getElementById("treinta").checked = true;
    //     document.getElementById("treinta").nextElementSibling.classList.add("check")
    // }
    // else if(valores.includes("cuota=48")){
    //     document.getElementById("cuarentaocho").checked = true;
    //     document.getElementById("cuarentaocho").nextElementSibling.classList.add("check")
    // }
    // else if(valores.includes("cuota=60")){
    //     document.getElementById("sesenta").checked = true;
    //     document.getElementById("sesenta").nextElementSibling.classList.add("check")
    // }
    
    
    if (valores.includes("combo=cocina")){
        document.getElementById("cocina").checked = true;
        document.getElementById("cocina").nextElementSibling.classList.add("check")
    }
    else if(valores.includes("combo=tecnologia")){
        document.getElementById("tecnologia").checked = true;
        document.getElementById("tecnologia").nextElementSibling.classList.add("check")
    }
    else if(valores.includes("combo=living")){
        document.getElementById("living").checked = true;
        document.getElementById("living").nextElementSibling.classList.add("check")
    }
    else if(valores.includes("combo=hogar")){
        document.getElementById("hogar").checked = true;
        document.getElementById("hogar").nextElementSibling.classList.add("check")
    }
    else if(valores.includes("combo=dormitorio")){
        document.getElementById("dormitorio").checked = true;
        document.getElementById("dormitorio").nextElementSibling.classList.add("check")
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

})




function desactiveCheck_marcas() {
    cuotas.forEach(element => element.nextElementSibling.classList.remove("check"));
  }

function desactiveCheck_combos() {
    combos.forEach(element => element.nextElementSibling.classList.remove("check"));
  }