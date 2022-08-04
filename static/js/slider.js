const items = document.querySelectorAll('.slider img');
const itemCount = items.length;
const nextItem = document.querySelector('.next');
const previousItem = document.querySelector('.previous');
var slider = document.querySelector(".slider");
var img = document.querySelectorAll(".slider img");
let count = 0;
calcDisplaySlider = -100/itemCount;
alert(calcDisplaySlider);

img.forEach(function(image){
  image.setAttribute("style","width:calc(100%/" + itemCount + ")");
})

arrayAtributosSlider =["width:"+ itemCount*100 +"%","transform: translateX("+calcDisplaySlider +"%)"]
function atributosSlider (elem,atributos){
  for (var i; atributos; i++){ 
    elem.setAttribute("style",i)
  }
}

atributosSlider(slider, arrayAtributosSlider);
// tamañoSlider = slider.setAttribute("style","width:"+ itemCount*100 +"%");

// displaySlider = slider.setAttribute("style","transform: translateX("+calcDisplaySlider +"%)")

