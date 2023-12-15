let menu_hamburger = document.querySelector('.header__nav ol label');
const menu_spans = document.querySelectorAll('.header__nav ol label > span')
const menu_check_display_nav = document.querySelector('.header__nav ol label > input')

let nav_display = document.querySelector('.header__nav > ol> label + .nav__items');
const items_nav = document.querySelectorAll(".nav__items > li")

items_nav.forEach(element =>{
    element.addEventListener("click", clean_display_nav)
});



menu_hamburger.addEventListener("change",function(){
    menu_hamburger.classList.toggle('active');
})

function clean_display_nav() {

    console.log(menu_spans)
    menu_spans.forEach(element => element.style.transition="none")
    nav_display.style.transition = "none"
    menu_check_display_nav.checked = false
    menu_hamburger.classList.remove('active');
    text.style.color ="#fff"
}





