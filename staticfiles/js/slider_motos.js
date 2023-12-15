const slider__motos = document.querySelector('.slider__motos');
const btnPrev = document.querySelector('.btn-prev');
const btnNext = document.querySelector('.btn-next');

const items = document.querySelectorAll('.item');
const contItem = items.length;

const rootStyles_for_motos = document.documentElement.style;


let slideCont = 0;
let transition = false;

const BUTTON = {
  RIGHT: 'RIGHT',
  LEFT: 'LEFT'
};

slider__motos.setAttribute("style","min-width:calc(100%/" + contItem + ")");
tamañoSlider = slider__motos.setAttribute("style","width:"+ contItem*100 +"%");
items.forEach(function(image){
  image.setAttribute("style","width:calc(100%/" + contItem + ")");
})
let operation = 0;
let calcDisplaySlider_moto = 100/contItem;


const valor_transform = () =>
  Number(rootStyles_for_motos.getPropertyValue('--slide-transform_moto').replace('%', ''));

const sliderOrder = () => {
  const transformValue = valor_transform();
  rootStyles_for_motos.setProperty('--transition_moto', 'none');
  if (slideCont === contItem - 1) {
    slider__motos.appendChild(slider__motos.firstElementChild);
    operation += (calcDisplaySlider_moto);
    rootStyles_for_motos.setProperty(
      '--slide-transform_moto',
      `${operation}%`
    );
    slideCont--;
  } else if (slideCont === 0) {
    slider__motos.prepend(slider__motos.lastElementChild);
    operation += -(calcDisplaySlider_moto);
    rootStyles_for_motos.setProperty(
      '--slide-transform_moto',
      `${operation}%`
    );
    slideCont++;
  }

  transition = false;
};

const slideDirection = direction => {
  if (transition) return;
  const transformValue = operation
  rootStyles_for_motos.setProperty('--transition_moto', 'transform 1s');
  transition = true;
  if (direction === BUTTON.LEFT) {
    operation += (calcDisplaySlider_moto);
    rootStyles_for_motos.setProperty(
      '--slide-transform_moto',
      `${operation}%`
    );
    slideCont--;
  } else if (direction === BUTTON.RIGHT) {
    operation += -(calcDisplaySlider_moto);
    rootStyles_for_motos.setProperty(
      '--slide-transform_moto',
      `${operation}%`
    );
    slideCont++;
  }
};



btnNext.addEventListener('click', () => slideDirection(BUTTON.RIGHT));
btnPrev.addEventListener('click', () => slideDirection(BUTTON.LEFT));

slider__motos.addEventListener('transitionend', sliderOrder);

sliderOrder();