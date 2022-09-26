const cv = document.querySelector("#cv");
const button_cv = document.querySelector("#cv_input");
var cv_element = document.createElement("h4");
const parent_cv = document.querySelector(".image_url")
const image_cv = document.querySelector(".cv_field label img")

button_cv.addEventListener("click",function(){
    cv.click()
})
// button_cv.addEventListener("touch",function(){
//     cv.touch()
// })
cv.addEventListener("change",function(){
    if (cv_element.textContent != "") {
        url = document.createTextNode(cv.value)
        cv_element.textContent = ""
        cv_element.appendChild(url)
    
    }
    else{
        let url = document.createTextNode(cv.value)
        cv_element.appendChild(url)
        parent_cv.appendChild(cv_element)
    }
    if (cv.value != "") {
        image_cv.removeAttribute("src")
        image_cv.setAttribute("src","/static/images/done.svg")
    }else{
        image_cv.removeAttribute("src")
        image_cv.setAttribute("src","/static/images/in_file.svg")
    }
    
})