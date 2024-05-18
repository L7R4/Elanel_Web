const slider = document.querySelector(".slides");
const sliderContainer = document.querySelector(".sliderContainer");
let slideElements = document.querySelectorAll(".slideElement");
const prev = document.querySelector("#prevButton");
const next = document.querySelector("#nextButton");

let totalSlides = slideElements.length;
let anchoPorSlide = 100 / totalSlides;
slider.style.width = `${totalSlides * 100}%`;

// Configura el ancho de cada slide
slideElements.forEach(element => {
    element.style.width = `${anchoPorSlide}%`;
    element.style.flexBasis = `${anchoPorSlide}%`;
});

let i = 0;

function moveToNextSlide() {
    slider.style.transition = 'transform 0.5s ease-in-out';
    i++;
    if (i >= totalSlides) {
        i = 0;
        console.log("weos")
    }
    slider.style.transform = `translateX(-${i * anchoPorSlide}%)`;
}

setInterval(moveToNextSlide, 4500);