const slider = document.querySelector(".slides")
const sliderContainer = document.querySelector(".sliderContainer")
let slideElements = document.querySelectorAll(".slideElement")
const prev = document.querySelector("#prevButton")
const next = document.querySelector("#nextButton")

// Calcula el ancho del container de slides
const totalSlides = slideElements.length;
slider.style.width = `${totalSlides * 100}%`;

// Calcula el ancho de los slide por separado
let anchoPorSlide = 0;
slideElements.forEach(element => {
    anchoPorSlide = 100/totalSlides
    element.style.width = `${anchoPorSlide}%`;
    element.style.flexBasis = `${anchoPorSlide}%`;
});

var direction;
prev.addEventListener('click', function(){
    if(direction === -1){
        slider.appendChild(slider.firstElementChild)
        direction = 1;

    }
    sliderContainer.style.justifyContent = 'flex-end'

    slider.style.transform = `translate(${anchoPorSlide}%)`
})
next.addEventListener('click', function(){
    direction = -1;
    sliderContainer.style.justifyContent = 'flex-start'
    slider.style.transform = `translate(-${anchoPorSlide}%)`
})

slider.addEventListener("transitionend", function() {
    if(direction === -1){
        slider.appendChild(slider.firstElementChild)

    }else if(direction === 1){
        slider.prepend(slider.lastElementChild)
    }

    slider.style.transition = 'none'
    slider.style.transform = 'translate(0)'
    setTimeout(function () {
        slider.style.transition = 'all 0.5s'
    })
})