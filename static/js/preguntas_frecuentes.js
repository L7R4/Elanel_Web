const questions = document.querySelectorAll(".question h2");
// var texts_heights = document.getElementsByClassName('texts');


questions.forEach(element => {
    element.addEventListener('click', ()=>{
        const height = element.nextElementSibling.scrollHeight;
        element.classList.toggle('active')
        if (element.classList.contains('active')) {
            element.nextElementSibling.style.maxHeight = height +'px'
            element.nextElementSibling.style.padding = '1% 0'
        }else{
            element.nextElementSibling.style.maxHeight = '0px'
            element.nextElementSibling.style.padding = '0'
        }
    });
});