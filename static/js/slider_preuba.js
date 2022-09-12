const items = document.querySelectorAll('.slider img');
const itemCount = items.length;
const nextItem = document.querySelector('.next');
const previousItem = document.querySelector('.previous');
let slider = document.querySelector(".slider");
var img = document.querySelectorAll(".slider img");

let count = 1;
let operacion = 0;
let calcDisplaySlider = 100/itemCount;
let clicked = false;

slider.setAttribute("style","min-width:calc(100%/" + itemCount + ")");
tamañoSlider = slider.setAttribute("style","width:"+ itemCount*100 +"%");
img.forEach(function(image){
  image.setAttribute("style","width:calc(100%/" + itemCount + ")");
})
previousItem.classList.add("disable");


// CUANDO EL SLIDE TIENE 1 O 2 POSTS
if(itemCount==2){
  nextItem.addEventListener("click",()=>{
    previousItem.classList.remove("disable");
    nextItem.classList.remove("disable")

})
}
if(itemCount==2){
  previousItem.addEventListener("click",()=>{
  nextItem.classList.remove("disable")

})

}
if(itemCount == 1){
  nextItem.classList.add("disable")
  previousItem.classList.add("disable")
}

// CUANDO EL SLIDE TIENE MAS DE 2 POSTS
function next(){
  // clicked =true;
  count++;
  if(count <= itemCount) {
    operacion += -(calcDisplaySlider);
    slider.style.transform = "translateX("+ operacion +"%)"
    console.log("contador" +count);
    console.log("operacion"+operacion);
    nextItem.classList.remove("disable")
    previousItem.classList.remove("disable")
  } 
else {
    count=1;
    operacion=0;
    slider.style.transform = "translateX("+ operacion +"%)"
  }
}

nextItem.addEventListener("click",next);


function previou() {
  count--;
  console.log("contador" +count);
  operacion += (calcDisplaySlider);
  console.log("operacion"+operacion);
  slider.style.transform = "translateX("+ operacion +"%)"
  previousItem.disabled=false;
  if(count > 1) {
    previousItem.classList.remove("disable")
    nextItem.classList.remove("disable")
  } else {
    previousItem.classList.add("disable");
  }
}
previousItem.addEventListener("click",previou);
  
// AUTOMATIZAR SLIDE
let cont= 1
let timerId=setInterval(()=>{
  next();
  cont++
  console.log(cont)
  if (cont == itemCount){
    cont = 0;
  }
  if (cont%itemCount == 0){
    previousItem.classList.add("disable");
  }
},3000);


// setTimeout(previou,3000);

// PARA BLOQUEAR EL USO DE ESPACIO Y ENTER
window.addEventListener("keydown", function(event){
  if (window.event.keyCode == 32 || window.event.keyCode == 13){
      event.preventDefault();
  }
},false);
