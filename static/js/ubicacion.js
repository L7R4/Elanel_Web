const ubications = document.querySelectorAll(".locales button");
const resistencia_button = document.querySelector("#resistencia");
let all_provincias = document.querySelectorAll(".mapa__container *");

const corrientes_map = document.querySelector("#mapa_corrientes");
const conrrientes_name = document.querySelector("#ubicacion__direccion_corrientes");
const text_corrientes = document.querySelector(".ubicacion__text_container.corrientes")

const resistencia_map = document.querySelector("#mapa_resistencia");
const resistencia_name = document.querySelector("#ubicacion__direccion_resistencia");
const text_resistencia = document.querySelector(".ubicacion__text_container.resistencia")

const posadas_map = document.querySelector("#mapa_posadas");
const posadas_name = document.querySelector("#ubicacion__direccion_posadas");
const text_posadas = document.querySelector(".ubicacion__text_container.posadas")

const saenzPenia_map = document.querySelector("#mapa_saenzPenia");
const saenzPenia_name = document.querySelector("#ubicacion__direccion_saenzPenia");
const text_saenzPenia = document.querySelector(".ubicacion__text_container.saenzPenia")

ubications.forEach(function(ubication){
    ubication.addEventListener("click",function(){
        desactiveUbicationButton()
        ubication.classList.add("active_ubication")
    
    if (ubication.classList.contains("resistencia")) {
        // alert("resiste")
        desactiveUbication() 
        text_resistencia.classList.add("active_provincia")
        resistencia_map.classList.add("active_provincia")
        resistencia_name.classList.add("active_provincia")

    }else if(ubication.classList.contains("corrientes")){
        // alert("corre")
        desactiveUbication() 
        text_corrientes.classList.add("active_provincia")
        corrientes_map.classList.add("active_provincia")
        conrrientes_name.classList.add("active_provincia")
    }
    else if(ubication.classList.contains("posadas")){
        // alert("corre")
        desactiveUbication() 
        text_posadas.classList.add("active_provincia")
        posadas_map.classList.add("active_provincia")
        posadas_name.classList.add("active_provincia")
    }else if(ubication.classList.contains("saenzPenia")){
        // alert("corre")
        desactiveUbication() 
        text_saenzPenia.classList.add("active_provincia")
        saenzPenia_map.classList.add("active_provincia")
        saenzPenia_name.classList.add("active_provincia")
    }
    })
})


function desactiveUbicationButton() {
    ubications.forEach(element => element.classList.remove("active_ubication"));
  }
function desactiveUbication() {
    all_provincias.forEach(element => element.classList.remove("active_provincia"));
  }
