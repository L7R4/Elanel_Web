const items = document.querySelectorAll('.slider img');
const itemCount = items.length;
const nextItem = document.querySelector('.next');
const previousItem = document.querySelector('.previous');
var slider = document.querySelector(".slider");
var img = document.querySelectorAll(".slider img");
let count = 0;

img.forEach(function(image){
  image.setAttribute("style","width:calc(100%/" + itemCount + ")");
})

tamañoSlider = slider.setAttribute("style","width:"+ itemCount*100 +"%");

// calcDisplaySlider = (itemCount*100)/itemCount;
// alert(calcDisplaySlider);

// displaySlider = slider.setAttribute("style","transform:")




// function showNextItem() {
//   items[count].classList.remove('active');

//   if(count < itemCount - 1) {
//     count++;
//   } else {
//     count = 0;
//   }

//   items[count].classList.add('active');
//   console.log(count);
// }

// function showPreviousItem() {
//   items[count].classList.remove('active');

//   if(count > 0) {
//     count--;
//   } else {
//     count = itemCount - 1;
//   }

//   items[count].classList.add('active');
//   console.log(count);
// }

// function keyPress(e) {
//   e = e || window.event;
  
//   if (e.keyCode == '37') {
//     showPreviousItem();
//   } else if (e.keyCode == '39') {
//     showNextItem();
//   }
// }

// nextItem.addEventListener('click', showNextItem);
// previousItem.addEventListener('click', showPreviousItem);
// document.addEventListener('keydown', keyPress);
