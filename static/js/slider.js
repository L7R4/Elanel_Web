const items = document.querySelectorAll('.slider img');
const itemCount = items.length;
const nextItem = document.querySelector('.next');
const previousItem = document.querySelector('.previous');
let slider = document.querySelector(".slider");
alert(itemCount)
var img = document.querySelectorAll(".slider img");
let count = 1;
let operacion =0;
calcDisplaySlider = 100/itemCount;
let clicked = false;

img.forEach(function(image){
  image.setAttribute("style","width:calc(100%/" + itemCount + ")");
  
})
previousItem.classList.add("disable");

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


nextItem.addEventListener("click",()=>{
  clicked =true;
  count++;
  console.log("contador" +count);
  operacion += -(calcDisplaySlider);
  console.log("operacion"+operacion);
  slider.style.transform = "translateX("+ operacion +"%)"
  if(count < itemCount) {
    nextItem.classList.remove("disable")
    previousItem.classList.remove("disable")
  } 
else {
    nextItem.classList.add("disable");
  }
  
})
previousItem.addEventListener("click",()=>{
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
})
  
tamañoSlider = slider.setAttribute("style","width:"+ itemCount*100 +"%");


window.addEventListener("keydown", function(event){
  if (window.event.keyCode == 32 || window.event.keyCode == 13){
      event.preventDefault();
  }
},false);