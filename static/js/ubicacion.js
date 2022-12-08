const ubications = document.querySelectorAll(".locales button");
const resistencia_button = document.querySelector("#resistencia");
let all_provincias = document.querySelectorAll(".mapa__container *");
const corrientes_map = document.querySelector("#mapa_corrientes");
const conrrientes_name = document.querySelector("#ubicacion__direccion_corrientes");
const resistencia_map = document.querySelector("#mapa_resistencia");
const resistencia_name = document.querySelector("#ubicacion__direccion_resistencia");


ubications.forEach(function(ubication){
    ubication.addEventListener("click",function(){
        desactiveUbicationButton()
        ubication.classList.add("active_ubication")
    
    if (ubication.classList.contains("resistencia")) {
        // alert("resiste")
        desactiveUbication() 
        resistencia_map.classList.add("active_provincia")
        resistencia_name.classList.add("active_provincia")

    }else if(ubication.classList.contains("corrientes")){
        // alert("corre")
        desactiveUbication() 
        corrientes_map.classList.add("active_provincia")
        conrrientes_name.classList.add("active_provincia")
    }
    })
})


function desactiveUbicationButton() {
    ubications.forEach(element => element.classList.remove("active_ubication"));
  }
function desactiveUbication() {
    all_provincias.forEach(element => element.classList.remove("active_provincia"));
  }
