var btn_categoria = document.querySelector(".items__menu");
var submenuCategoria = document.querySelector(".menu_categoria");
const btn_categoria_img = document.querySelector(".items__menu img");
const text = document.querySelector(".items__menu a");

// BOTON DE CATEGORIAS
btn_categoria.addEventListener("mouseover",function(){
    btn_categoria_img.style.transform = "rotate(180deg)"
    btn_categoria_img.style.transition = "all 0.2s ease-in";
    submenuCategoria.style.visibility = "visible";
    text.style.color ="#027cf1";
})
btn_categoria.addEventListener("mouseout",function(){
    // submenuCategoria.style.zIndex = "-1";
    btn_categoria_img.style.transform = "rotate(0deg)"
    btn_categoria_img.style.transition = "all 0.1s ease-in";
    text.style.color ="#fff";
    submenuCategoria.style.visibility = "hidden";
})
