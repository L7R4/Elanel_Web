// BUTTONS
const back = document.getElementById("button-left");
const forward = document.getElementById("button-right");
// -------


let slider = document.querySelector(".slider");
let items_slider = document.querySelectorAll(".slider__element");
let lastElement = slider.lastElementChild;
let firstElement = slider.firstElementChild;

let lastElement_clone = slider.lastElementChild.cloneNode(true);
let firstElement_clone = slider.firstElementChild.cloneNode(true);

let length_slider = items_slider.length;
let length_slider_for_to_items = length_slider * 2;

const mqLarge  = window.matchMedia( '(min-width: 600px)' );
let size = mqLarge.matches ? 'large' : 'not large'
if (size == "not large"){
  slider = document.querySelector(".slider_cel");
  items_slider = document.querySelectorAll(".slider__element_cel");
  lastElement = slider.lastElementChild;
  firstElement = slider.firstElementChild;

  lastElement_clone = slider.lastElementChild.cloneNode(true);
  firstElement_clone = slider.firstElementChild.cloneNode(true);

  length_slider = items_slider.length;
  length_slider_for_to_items = length_slider * 2;
}


if (length_slider === 2) {
  slider.setAttribute(
    "style",
    "width:" + length_slider_for_to_items * 100 + "%"
  );
  slider.insertAdjacentElement("beforeend", lastElement_clone);
  slider.insertAdjacentElement("beforeend", firstElement_clone);
} else {
  slider.setAttribute("style", "width:" + length_slider * 100 + "%");
}
slider.insertAdjacentElement("afterbegin", lastElement);


// media query handler function
function mqHandler(e) {
  let size = e.matches ? 'large' : 'not large'
  console.log(size);
  if (size == "not large") {
    slider = document.querySelector(".slider_cel");
    items_slider = document.querySelectorAll(".slider__element_cel");
    lastElement = slider.lastElementChild;
    firstElement = slider.firstElementChild;

    lastElement_clone = slider.lastElementChild.cloneNode(true);
    firstElement_clone = slider.firstElementChild.cloneNode(true);

    length_slider = items_slider.length;
    length_slider_for_to_items = length_slider * 2;
    if (length_slider === 2) {
      slider.setAttribute(
        "style",
        "width:" + length_slider_for_to_items * 100 + "%"
      );
      slider.insertAdjacentElement("beforeend", lastElement_clone);
      slider.insertAdjacentElement("beforeend", firstElement_clone);
    } else {
      slider.setAttribute("style", "width:" + length_slider * 100 + "%");
    } 
  }else{
    slider = document.querySelector(".slider");
    items_slider = document.querySelectorAll(".slider__element");
    lastElement = slider.lastElementChild;
    firstElement = slider.firstElementChild;

    lastElement_clone = slider.lastElementChild.cloneNode(true);
    firstElement_clone = slider.firstElementChild.cloneNode(true);

    length_slider = items_slider.length;
    length_slider_for_to_items = length_slider * 2;
    if (length_slider === 2) {
      slider.setAttribute(
        "style",
        "width:" + length_slider_for_to_items * 100 + "%"
      );
      slider.insertAdjacentElement("beforeend", lastElement_clone);
      slider.insertAdjacentElement("beforeend", firstElement_clone);
    } else {
      slider.setAttribute("style", "width:" + length_slider * 100 + "%");
    } 
  }
  slider.insertAdjacentElement("afterbegin", lastElement);  
}



function nextItem() {
  let size = mqLarge.matches ? 'large' : 'not large'
  if (size == "not large") {
    firstElement = document.querySelectorAll(".slider__element_cel")[0];
  }else{
    firstElement = document.querySelectorAll(".slider__element")[0];
  }
  slider.setAttribute(
    "style",
    "width:" +
      (length_slider == 2
        ? length_slider_for_to_items * 100
        : length_slider * 100) +
      "%;" +
      "margin-left: -200%;"
  );
  setTimeout(() => {
    slider.setAttribute(
      "style",
      "transition: none;" +
        "width:" +
        (length_slider == 2
          ? length_slider_for_to_items * 100
          : length_slider * 100) +
        "%;" +
        "margin-left: -100%;"
    );
    slider.insertAdjacentElement("beforeend", firstElement);
  }, 1000);
}

function backItem() {
  let size = mqLarge.matches ? 'large' : 'not large'
  if (size == "not large") {
    let items_slider = document.querySelectorAll(".slider__element_cel");
    lastElement = document.querySelectorAll(".slider__element_cel")[items_slider.length - 1];
  }else{

    let items_slider = document.querySelectorAll(".slider__element");
    lastElement = document.querySelectorAll(".slider__element")[items_slider.length - 1];
  }
  
  slider.setAttribute(
    "style",
    "width:" +
      (length_slider == 2
        ? length_slider_for_to_items * 100
        : length_slider * 100) +
      "%;" +
      "margin-left: 0%;"
  );
  setTimeout(() => {
    slider.insertAdjacentElement("afterbegin", lastElement);
    slider.setAttribute(
      "style",
      "transition: none;" +
        "width:" +
        (length_slider == 2
          ? length_slider_for_to_items * 100
          : length_slider * 100) +
        "%;" +
        "margin-left: -100%;"
    );
  }, 1000);
}

// EVENTS
// let timerId=setInterval(nextItem,6000);
mqLarge.addEventListener('change', mqHandler);
back.addEventListener("click", backItem);
forward.addEventListener("click", nextItem);
// ----------
