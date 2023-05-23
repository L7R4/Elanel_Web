const button_filter = document.getElementById("filter_button");
const filter_nav = document.querySelector(".filters_container")
button_filter.addEventListener("click", () =>{
    filter_nav.classList.toggle("active")
    if (filter_nav.classList.contains("active")) {
        setTimeout(()=>{
            button_filter.textContent="Cerrar";
        },200)
    }else{
        setTimeout(()=>{
            button_filter.textContent="Filtrar";
        },200)
    }
})