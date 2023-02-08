let lists_products = document.querySelectorAll(".beneficios__table__item__products > .title_select")
let all_products = document.querySelectorAll(".beneficios__table__item__products > .list_products > li")
let productos;
fetch("/m/categorias/beneficios/",{
    method: 'get',
    headers: {'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/json' ,}
}).then(
    function(response){
        return response.json()
    }
).then(data =>{
    all_products.forEach(element => {
        element.addEventListener("click",() =>{
            product = element.children[0].textContent
            producto_seleccionado = data.filter((producto)=> producto.nombre == product)
            monto_del_producto = producto_seleccionado[0].monto_total

            element.parentElement.parentElement.previousElementSibling.textContent = "$" + Math.trunc(monto_del_producto) + "/mes"
            
            element.parentElement.previousElementSibling.children[0].textContent = producto_seleccionado[0].nombre
        })
    });
})


lists_products.forEach(element => {
    element.addEventListener('click', ()=>{
        const height = element.nextElementSibling.scrollHeight;
        element.classList.toggle('active')
        if (element.classList.contains('active')) {
            element.nextElementSibling.style.maxHeight = height +'px'
            element.nextElementSibling.style.padding = '1% 0'
        }else{
            element.nextElementSibling.style.maxHeight = '0px'
            element.nextElementSibling.style.padding = '0'
        }
    });
});