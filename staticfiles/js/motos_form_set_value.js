const url_product = window.location.pathname

let input_target = document.querySelector("#objetivo")
let inputs_wrapper = input_target.offsetParent.parentElement.previousElementSibling


window.addEventListener('load',()=>{
    if (url_product.includes("elec")){
        
        let input_target_elec = inputs_wrapper.children[1].children[0].children[0].textContent
        
        let input_target_precio = inputs_wrapper.children[1].children[0].children[1].textContent
    
        input_target_elec = "Equipo " + input_target_elec + " a " + input_target_precio
        try{
            let input_target_marca = inputs_wrapper.children[1].children[1].children[0].children[1].textContent
            input_target_elec = "Equipo " + input_target_elec + " " + input_target_marca + " a " + input_target_precio
            
            console.log(input_target_elec)
        }catch{
        }
        input_target.value = input_target_elec
    
        
    
    
    }else if(url_product.includes("motos")){
        let input_target_moto = inputs_wrapper.children[1].children[0].children[0].textContent
    
        let input_target_marca = inputs_wrapper.children[1].children[1].children[0].children[1].textContent
        
        let input_target_modelo = inputs_wrapper.children[1].children[1].children[1].children[1].textContent
        
        let input_target_precio = inputs_wrapper.children[1].children[0].children[1].textContent
    
        input_target_moto = "Moto " + input_target_moto + " " + input_target_modelo + " " + input_target_marca + " a " + input_target_precio
        console.log(input_target_moto)
        input_target.value = input_target_moto
    }

})



