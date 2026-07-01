let lists_products = document.querySelectorAll(".beneficios__table__item__products > .title_select")
let all_products = document.querySelectorAll(".beneficios__table__item__products > .list_products > li")
let productos;
window.addEventListener('load',()=>{
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
                const product = element.children[0].textContent.trim();
                const parentItem = element.closest(".beneficios__table__item");
                const serviceName = parentItem.getAttribute("data-service") || "Servicio Mecánico";
                
                // Update select title label
                element.parentElement.previousElementSibling.children[0].textContent = product;
                
                // Enable and configure WhatsApp button
                const waBtn = parentItem.querySelector(".beneficios__whatsapp-btn");
                if (waBtn) {
                    waBtn.classList.remove("disabled");
                    const textMessage = `Hola! Me interesa el *${serviceName}* para el producto *${product}*.\n\n¿Me podrían asesorar?`;
                    waBtn.href = `https://wa.me/543625170890?text=${encodeURIComponent(textMessage)}`;
                }
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

})