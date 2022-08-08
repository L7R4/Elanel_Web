const menu = document.querySelectorAll(".menu > div");
const detalle = document.querySelectorAll(".detalle > div")

let index = 1;
menu.forEach(function(item){
    item.addEventListener("click",function(){
        desactiveMenu();
        let menuActive= item.classList.add("active");
        console.log({item})
        // let sd= item.classList.contains("soluciones_dinerarias")
        // console.log(sd)

        if(item.classList.contains("soluciones_dinerarias")){
            desactiveDetalle();
            const detalleSoluciones_dinerarias = document.querySelector(".detalle__soluciones_dinerarias_contenido");
            detalleSoluciones_dinerarias.classList.add("active");
         }
         else if(item.classList.contains("electrodomesticos")){
            desactiveDetalle();
            const detalleElectrodomesticos = document.querySelector(".detalle__electrodomesticos_contenido");
            detalleElectrodomesticos.classList.add("active");
         }
         else if(item.classList.contains("motos")){
            desactiveDetalle();
            const detalleMotos = document.querySelector(".detalle__motos_contenido");
            detalleMotos.classList.add("active");
         }
         else if(item.classList.contains("beneficios")){
            desactiveDetalle();
            const detalleBeneficios = document.querySelector(".detalle__beneficios_contenido");
            detalleBeneficios.classList.add("active");
         }
    });
});
function desactiveMenu() {
    menu.forEach(element => element.classList.remove("active"));
  }
function desactiveDetalle() {
    detalle.forEach(element => element.classList.remove("active"));
  }