const items = document.querySelectorAll('.slider img');
const itemCount = items.length;
const nextItem = document.querySelector('.next');
const previousItem = document.querySelector('.previous');
var slider = document.querySelector(".slider");

var img = document.querySelectorAll(".slider img");
let count = 0;
calcDisplaySlider = -100/itemCount;
alert(calcDisplaySlider);

img.forEach(function(image,i){
  image.setAttribute("style","width:calc(100%/" + itemCount + ")");
  console.log(i);
  nextItem.addEventListener("click",()=>{
    operacion += i * calcDisplaySlider 
    slider.style.transform = "translateX("+ operacion +"%)"
    // if(itemCount< i + 1){
    //   calcDisplaySlider = 0;
    // }
  })
})


// Object.assign(slider.style,{width:itemCount*100 +"%",transform:"translateX(" + calcDisplaySlider +"%)"});

tamañoSlider = slider.setAttribute("style","width:"+ itemCount*100 +"%");

// slider.style.transform = "translateX("+ operacion +"%)"

