const menu = document.querySelectorAll(".menu > div");
menu.forEach(item,i=>{
    item.addEventListener("click",function(){
        console.log(i)
        menuActive =item.classList.add("active");
        console.log({item})
        // if(menuActive.classList.contains("motos")){

        // }
    });
});