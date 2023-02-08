// BUTTONS
const back_button = document.getElementById("back");
const forward_button = document.getElementById("forward");
// -------

const slider_adju = document.querySelector(".slider_adjudicado");
let items_slider_adju = document.querySelectorAll(".item_adjudicado2");
let lastElement_adju = slider_adju.lastElementChild;
let firstElement_adju = slider_adju.firstElementChild;

let lastElement_clone_adju = slider_adju.lastElementChild.cloneNode(true);
let firstElement_clone_adju = slider_adju.firstElementChild.cloneNode(true);

const length_slider_adju = items_slider_adju.length;
const length_slider_for_to_items_adju = length_slider_adju * 2;

if (length_slider_adju === 2) {
  slider_adju.setAttribute(
    "style",
    "width:" + length_slider_for_to_items_adju * 100 + "%"
  );
  slider_adju.insertAdjacentElement("beforeend", firstElement_clone_adju);
  slider_adju.insertAdjacentElement("beforeend", lastElement_clone_adju);
} else {
  slider_adju.setAttribute("style", "width:" + length_slider_adju * 100 + "%");
  slider_adju.insertAdjacentElement("afterbegin", lastElement_adju);
}


function nextItem() {
  firstElement_adju = document.querySelectorAll(".item_adjudicado2")[0];
  slider_adju.setAttribute(
    "style",
    "width:" +
      (length_slider_adju == 2
        ? length_slider_for_to_items_adju * 100
        : length_slider_adju * 100) +
      "%;" +
      "margin-left: -200%;"
  );
  setTimeout(() => {
    slider_adju.setAttribute(
      "style",
      "transition: none;" +
        "width:" +
        (length_slider_adju == 2
          ? length_slider_for_to_items_adju * 100
          : length_slider_adju * 100) +
        "%;" +
        "margin-left: -100%;"
    );
    slider_adju.insertAdjacentElement("beforeend", firstElement_adju);
  }, 1000);
}

function backItem() {
  let items_slider_adju = document.querySelectorAll(".item_adjudicado2");
  lastElement_adju =
    document.querySelectorAll(".item_adjudicado2")[items_slider_adju.length - 1];
  slider_adju.setAttribute(
    "style",
    "width:" +
      (length_slider_adju == 2
        ? length_slider_for_to_items_adju * 100
        : length_slider_adju * 100) +
      "%;" +
      "margin-left: 0%;"
  );
  setTimeout(() => {
    slider_adju.insertAdjacentElement("afterbegin", lastElement_adju);
    slider_adju.setAttribute(
      "style",
      "transition: none;" +
        "width:" +
        (length_slider_adju == 2
          ? length_slider_for_to_items_adju * 100
          : length_slider_adju * 100) +
        "%;" +
        "margin-left: -100%;"
    );
  }, 1000);
}

// EVENTS
// let timerId=setInterval(nextItem,6000);
back_button.addEventListener("click", backItem);
forward_button.addEventListener("click", nextItem);
// ----------
