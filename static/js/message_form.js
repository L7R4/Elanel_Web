const form_product = document.querySelector("#form_product")

form_product.addEventListener("submit", async ()=>{
    Swal.fire({
        title: '¡Muchas gracias!',
        text: 'Nos comunicaremos contigo en un momento',
        icon: 'success',
        // color:'red'
        iconColor: '#027df1',
        width:'40%',
        // height:'300px',
        padding: '5% 5%',
        confirmButtonText:'Salir',
      })

})
